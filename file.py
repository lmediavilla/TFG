# coding utf-8

from telegram.ext import CommandHandler, Updater
from telegram import ChatAction
from cambio import Bolsa
from Mercado import Accion
from Noticias import Noticias
import inspect
import datetime
from sys import argv
import pandas as pd
from Syslog import Syslog
from Alerta import Alerta


#devolver un hola al usuario
def hola_comando(bot, update):
    update.message.reply_text(
        'Hola {}, por ahora soporto:\n /hola \n/adios \n/cambio \n/noticias \n/valor empresa \n/alerta'.format(f'@{update.message.from_user.username}'))

def debug_comando(bot, update):
    print(f'user: @{update.message.from_user.username}')
    print(f'chatid: {update.message.chat_id}')
    update.message.reply_text(f'user: @{update.message.from_user.username} \n chatid: {update.message.chat_id}')
#devolver un adios al usuario
def adios_comando(bot, update):
    update.message.reply_text(
        'Adios {}'.format(update.message.from_user.first_name))

#devolver cambio al usuario
def cambio_comando(bot, update, args):
    if len(args) == 0:
        update.message.reply_text('Los cambios aceptados son entre éste tipo de monedas: \n EUR -> EURO  \n USD -> DOLAR AMERICANO \n JPY -> YEN JAPONES  \nCHF -> FRANCO SUIZO \n AUD -> DOLAR AUSTRALIANO \n CAD -> DOLAR CANADIENSE \n NZD -> DOLAR NEOZENLANDES \n  GBP -> LIBRA INGLESA \n SEK -> CORONA SUECA \n NOK -> CORONA NORUEGA \n MXN -> PEXO MEXICANO \n TRY -> LIRA TURCA \n ZAR -> RAND SUDAFRICANO\n CNH -> YUAN CHINO\n XAU -> ONZA DE ORO \n XAG -> ONZA DE PLATA \nSGD -> DOLAR SINGAPUR \nRUB -> RUBLO RUSO \nHKD -> DOLAR DE HONG KONG \nDKK -> CORONA DANESA \nPLN -> POLACA \n BTC -> BitCoin  (CRIPTO)\nETH -> Etherum  (CRIPTO)\nLTC -> LittleCoin  (CRIPTO)\nXRP -> RIPPLE (CRIPTO) \nDSH -> DASH (CRIPTO) \n BCH -> BITCOIN CASH (CRIPTO)\n')
    if len(args) == 2:
        moneda1, moneda2 = args
        moneda1 = moneda1.upper()
        moneda2 = moneda2.upper()
        C = Bolsa()
        update.message.reply_text(C.cambio(moneda1, moneda2))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /cambio moneda1 moneda2')

def cambioayuda_comando(bot, update,):
        update.message.reply_text('Los cambios aceptados son entre éste tipo de monedas: \n EUR -> EURO  \n USD -> DOLAR AMERICANO \n JPY -> YEN JAPONES  \nCHF -> FRANCO SUIZO \n AUD -> DOLAR AUSTRALIANO \n CAD -> DOLAR CANADIENSE \n NZD -> DOLAR NEOZENLANDES \n  GBP -> LIBRA INGLESA \n SEK -> CORONA SUECA \n NOK -> CORONA NORUEGA \n MXN -> PEXO MEXICANO \n TRY -> LIRA TURCA \n ZAR -> RAND SUDAFRICANO\n CNH -> YUAN CHINO\n XAU -> ONZA DE ORO \n XAG -> ONZA DE PLATA \nSGD -> DOLAR SINGAPUR \nRUB -> RUBLO RUSO \nHKD -> DOLAR DE HONG KONG \nDKK -> CORONA DANESA \nPLN -> POLACA \n BTC -> BitCoin  (CRIPTO)\nETH -> Etherum  (CRIPTO)\nLTC -> LittleCoin  (CRIPTO)\nXRP -> RIPPLE (CRIPTO) \nDSH -> DASH (CRIPTO) \n BCH -> BITCOIN CASH (CRIPTO)\n')        

#noticias
def noticias_comando(bot, update, args):
    Log = Syslog()
    if len(args) == 1:
        #print('MAIN NOTICIAS')
        try:
            #print(f'args[0] -> {args[0]}')
            C = Noticias()
            valor = args[0]
            noticias = []
            #print(f'C.rss(valor) -> {C.rss(valor)}')
            noticias = C.rss(valor)
            #print(f'file.py noticias -> {noticias}')
            for i in range(len(noticias)):
                #print(f'{noticias[i]}')
                update.message.reply_text(f'{noticias[i]}')
            #chequeamos si está vacío
            if not noticias:
                update.message.reply_text('Ocurrió un error')
        except Exception as ex:
            print(f'file: noticias_comando -> {datetime.datetime.now().time()}: {ex}')
            Log.errorlog(f'file: noticias_comando ->  {ex}')
            update.message.reply_text('Ocurrió un error')
    else:
        try:
            C = Noticias()
            Array = []
            Array = C.lista()
            res = ''
            #print(f'len(Array): {len(Array)} Array: {Array}')
            for i in range(len(Array)):
                #print(f'Array[i]: {Array[i]}')
                res+=str(i)
                res+=str('->')
                res+=str(Array[i])
                res+=str('\n')
            #print(f'res: {res}')
            update.message.reply_text(f'Utiliza /noticias #numero siendo éste el proveedor de noticias\n {res}')
        except Exception as ex:
            update.message.reply_text(f'file: noticias_comando -> {datetime.datetime.now().time()}: {ex}')
            print(f'file: noticias_comando ->  {ex}')
            Log.errorlog(f'file: noticias_comando ->  {ex}')

#acción
def valor_comando(bot, update, args):
    if len(args) == 1:
        C = Accion()
        #print(C.valor(args[0]))
        update.message.reply_text(C.valor(args[0]))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')

def alerta_comando(bot, update, args):
    Log = Syslog()
    print(f'argumentos pasados {len(args)}')
    for i in range(len(args)):
        print(f'{i} -> {args[i]}')
    error = 'Comando erroneo, por favor utiliza:\n/alerta empresa < cantidad -> para crear una alerta \n/alerta listar -> para listar tus alertas \n/alerta borrar todas -> para borrar todas tus alertas \n/alerta borrar empresa < 1000 -> borra esa alerta'
    if len(args) == 0:
        #comando basico
        print('cero')
        Log.log('file -> alerta_comando "/alerta" ejecutado')
        update.message.reply_text(error)
    elif len(args) == 1:
        #comando listar (como mucho)
        print('uno')
        if args[0] == 'listar':
            print('listar')
            alerta = Alerta()
            array = []
            array =  alerta.listar(update.message.chat_id)
            if not array:
                update.message.reply_text("no hay alertas para mostrar")
            str = ''
            for i in range(len(array)):
                str = str + (f'{array[i]}\n')
            #print(str)
            update.message.reply_text(f'Listado de alertas pendientes: \n{str}')
        else:
            Log.log(f'file -> alerta_comando "/alerta {args[0]}" ejecutado')
            update.message.reply_text(error)
    elif len(args) == 2:
        print('dos')
        alerta = Alerta()
        #comando borrar mas id o todas
        Log.log(f'file -> alerta_comando "/alerta {args[0]} {args[1]}" ejecutado')
        if args[0] == 'borrar' and args[1] == 'todas':
            print('borrar todas')
            if alerta.borrar_todo(update.message.chat_id):
                print('Alertas creadas para éste chat borradas')
                update.message.reply_text('Alertas creadas para éste chat borradas')
            else:
                Log.errorlog(f'file -> alerta_comando "/alerta {args[0]} {args[1]}" ejecutado')
        elif args[0] == 'borrar':
            print('borrar')
            Id = int(args[1])
            if alerta.borrar(update.message.chat_id, Id):
                print('Alertas creadas para éste chat borradas')
                array =  alerta.listar(update.message.chat_id)
                str = ''
                for i in range(len(array)):
                    str = str + (f'{array[i]}\n')
                update.message.reply_text(f'Alerta borrada\nListado de alertas pendientes: \n{str}')
            else:
                Log.errorlog(f'file -> alerta_comando "/alerta {args[0]} {args[1]}" ejecutado')
        else:
            update.message.reply_text(error)
    elif len(args) == 3:
        print('tres')
        #comando msft > 1000def add(self, chatId, empresa, modificador, valor)
        alerta = Alerta()
        empresa = args[0]
        empresa = empresa.upper()
        modificador = args[1]
        valor = float(args[2])
        if(alerta.add(update.message.chat_id,empresa,modificador,valor)==True):
            Log.log(f'file -> alerta_comando "/alerta {args[0]} {args[1]} {args[2]} {args[3]}" ejecutado')
            update.message.reply_text('Alerta añadida')
            print('Alerta añadida')
        else:
            update.message.reply_text('Comando erroneo, por favor utiliza:\n /alerta  empresa > ó < cantidad')
            print('Alerta no añadida')
    else:
        print('no se')
        Log.errorlog('file -> alerta_comando comando mal introducido')
        update.message.reply_text(error)

def alerta_hilo(bot, job):
    Log = Syslog()
    Respuesta =[]
    #tenemos que buscar tareas pendientes de hacer
    C = Alerta()
    try:
        Respuesta = C.comprobar()
        for i in range((len(Respuesta))):
            chatId = int(Respuesta[i][0])
            Empresa = Respuesta[i][1]
            modificador = Respuesta[i][2]
            valor = float(Respuesta[i][3])
            vactual = float(Respuesta[i][4])
            Id = int(Respuesta[i][5])
            bot.send_message(chatId,f'Alerta\n{Empresa} {modificador} {valor}\nValor actual: {vactual}')
            C.borrar(chatId,Id)
            #print(Respuesta)
            #devolver respusta chaid, empresa, modificador, valor, valor actual, id a borrar
            #bot.send_message(chatid, text='<a href="http://link.to/image.png">\u200B</a>Rest of your text here blah blah blah', parse_mode='HTML')
    except Exception as ex:
        print(f'file: alerta_hilo ->  {ex}')
        Log.errorlog(f'file: alerta_hilo ->  {ex}')
        print(repr(ex))
        if repr(ex) == 'BadRequest()':
            print(chatId)
            print(Id)
            C.borrar(chatId,Id)
            Log.log(f'file: alerta_hilo ->  alerta borrada, el chat no existe')


def main(args):
    API1 = ''
    with open('./token1.txt', 'rU') as f:
        API1 = f.readline()
        #para linux
        API1 = API1.rstrip('\n')
        f.close()
    #print(f'API-1->{API1}')
    updater = Updater(API1)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('noticias',noticias_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('hola', hola_comando))
    dispatcher.add_handler(CommandHandler('alerta',alerta_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('start', hola_comando))
    dispatcher.add_handler(CommandHandler('adios', adios_comando))
    dispatcher.add_handler(CommandHandler('cambio',cambio_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('cambioayuda',cambioayuda_comando))
    dispatcher.add_handler(CommandHandler('valor', valor_comando, pass_args = True))
    dispatcher.add_handler(CommandHandler('debug', debug_comando))
    updater.start_polling(clean=True)
    j = updater.job_queue
    job_minute = j.run_repeating(alerta_hilo, interval=60, first=0)
    updater.idle()

if __name__ == '__main__':
    main(argv)