# coding utf-8

from telegram.ext import CommandHandler, Updater
from telegram import ChatAction
from telegram import ReplyKeyboardMarkup
from telegram import ParseMode
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
    custom_keyboard = [['/menu_principal'],['/cambio', '/noticias'],['/valor', '/alerta']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    respuesta = f'Hola @{update.message.from_user.username}, las funciones implementadas son:\n /hola \n/adios \n/cambio \n/noticias \n/valor\n/alerta'
    bot.send_message(update.message.chat_id, text=respuesta, reply_markup=reply_markup)
    #update.message.reply_text('Hola {}, por ahora soporto:\n /hola \n/adios \n/cambio \n/noticias \n/valor\n/alerta'.format(f'@{update.message.from_user.username}'))

def comandos_comando(bot, update):
    custom_keyboard = [['/menu_principal'],['/cambio', '/noticias'],['/valor', '/alerta']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    respuesta = f'Hola @{update.message.from_user.username}, las funciones implementadas son:\n /hola \n/adios \n/cambio \n/noticias \n/valor\n/alerta'
    bot.send_message(update.message.chat_id, text=respuesta, reply_markup=reply_markup)
    #update.message.reply_text('Hola {}, por ahora soporto:\n /hola \n/adios \n/cambio \n/noticias \n/valor\n/alerta'.format(f'@{update.message.from_user.username}'))


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
    respuesta = ''
    if len(args) == 0:
        custom_keyboard = [['/menu_principal'],['/cambio'], ['/cambio EUR USD','/CAMBIO EUR GBP'],['/cambio EUR JPY', '/cambio BTC EUR']]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        respuesta = 'Los cambios aceptados son entre éste tipo de monedas: \n*EUR* -> EURO  \n*USD* -> DOLAR AMERICANO \n*JPY* -> YEN JAPONES  \n*CHF* -> FRANCO SUIZO \n*AUD* -> DOLAR AUSTRALIANO \n*CAD* -> DOLAR CANADIENSE \n*NZD* -> DOLAR NEOZENLANDES \n*GBP* -> LIBRA INGLESA \n*SEK* -> CORONA SUECA \n*NOK* -> CORONA NORUEGA \n*MXN* -> PEXO MEXICANO \n*TRY* -> LIRA TURCA \n*ZAR* -> RAND SUDAFRICANO\n*CNH* -> YUAN CHINO\n*XAU* -> ONZA DE ORO \n*XAG* -> ONZA DE PLATA \n*SGD* -> DOLAR SINGAPUR \n*RUB* -> RUBLO RUSO \n*HKD* -> DOLAR DE HONG KONG \n*DKK* -> CORONA DANESA \n*PLN* -> POLACA \n*BTC* -> BitCoin  (CRIPTO)\n*ETH* -> Etherum  (CRIPTO)\n*LTC* -> LittleCoin  (CRIPTO)\n*XRP* -> RIPPLE (CRIPTO) \n*DSH* -> DASH (CRIPTO) \n*BCH* -> BITCOIN CASH (CRIPTO)\n'
        #bot.send_message(update.message.chat_id, text=respuesta, reply_markup=reply_markup)
        update.message.reply_text(text=respuesta, parse_mode=ParseMode.MARKDOWN,reply_markup=reply_markup)
    if len(args) == 2:
        Log = Syslog()
        try:
            moneda1, moneda2 = args
            moneda1 = moneda1.upper()
            moneda2 = moneda2.upper()
            C = Bolsa()
            respuesta = C.cambio(moneda1, moneda2)
            update.message.reply_text(text=respuesta, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            Log.errorlog(f"file -> cambio_comando -> {ex}")
            print(f"file -> cambio_comando -> {ex}")
            update.message.reply_text(f'No se pudo calcular el cambio entre {moneda1} y {moneda2}')
    else:
        update.message.reply_text('Por favor utiliza:\n /cambio moneda1 moneda2')

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
            respuesta = ''
            for i in range(len(noticias)):
                #print(f'{noticias[i]}')
                #respuesta = respuesta + noticias[i]
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
            respuesta = f'Utiliza /noticias #numero siendo éste el proveedor de noticias\n {res}'
            custom_keyboard = [['/menu_principal'],['/noticias'],['/noticias 0', '/noticias 1'],['/noticias 2', '/noticias 3']]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard)
            print('file -> noticias_comando: desplegando teclado /noticias')
            Log.log('file -> noticias_comando: desplegando teclado /noticias')
            bot.send_message(update.message.chat_id, text=f'{respuesta}', reply_markup=reply_markup)
            reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        except Exception as ex:
            update.message.reply_text(f'file: noticias_comando -> {datetime.datetime.now().time()}: {ex}')
            print(f'file: noticias_comando ->  {ex}')
            Log.errorlog(f'file: noticias_comando ->  {ex}')

#acción
def valor_comando(bot, update, args):
    Log = Syslog()
    if len(args) == 1:
        C = Accion()
        empresa = args[0]
        empresa = empresa.upper()
        #print(C.valor(args[0]))
        #respuesta = C.valor(empresa)+'\nhttps://finance.yahoo.com/quote/'+f'{args[0]}'
        if(C.valor(empresa) != 'error'):
            update.message.reply_text(C.valor(empresa)+'\nhttps://finance.yahoo.com/chart/'+f'{args[0]}',parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text(f'No podemos obtener el valor de {args[0]}')
    else:
        custom_keyboard = [['/menu_principal'],['/valor'],['/valor AMZN', '/valor AAPL'],['/valor GOOGL', '/valor ^IBEX']]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        print('file -> valor_comando: desplegando teclado /valor')
        Log.log('file -> valor_comando: desplegando teclado /valor')
        bot.send_message(update.message.chat_id, text=f'Por favor utiliza:\n /valor empresa', reply_markup=reply_markup)
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)

def alerta_comando(bot, update, args):
    Log = Syslog()
    print(f'argumentos pasados {len(args)}')
    for i in range(len(args)):
        print(f'{i} -> {args[i]}')
    error = 'Por favor utiliza:\n/alerta empresa < cantidad -> para crear una alerta \n/alerta listar -> para listar tus alertas \n/alerta borrar todas -> para borrar todas tus alertas \n/alerta borrar empresa < 1000 -> borra esa alerta'
    uso = 'utiliza:\n/alerta empresa < cantidad -> para crear una alerta \n/alerta listar -> para listar tus alertas \n/alerta borrar todas -> para borrar todas tus alertas \n/alerta borrar empresa < 1000 -> borra esa alerta'
    if len(args) == 0:
        #comando basico
        print('cero')
        Log.log('file -> alerta_comando "/alerta" ejecutado')
        custom_keyboard = [['/menu_principal'],['/alerta'],['/alerta listar'],['/alerta borrar todas'],['/alerta AMZN < 2000','/alerta GOOGL > 2000']]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        bot.send_message(update.message.chat_id, text=f'{uso}', reply_markup=reply_markup)
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        print('file -> alerta_comando: desplegando teclado /alerta')
        Log.log('file -> alerta_comando: desplegando teclado /alerta')
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
        res = alerta.add(update.message.chat_id,empresa,modificador,valor)
        if (res == True):
            Log.log(f'file -> alerta_comandoalerta {args[0]} {args[1]} {args[2]} ejecutado')
            print(f'file -> alerta_comando /alerta {args[0]} {args[1]} {args[2]} ejecutado')
            update.message.reply_text(f'Alerta añadida\n{empresa} {modificador} {valor}',parse_mode=ParseMode.MARKDOWN)
            #update.message.reply_text('Alerta añadida\n')
            #C.valor(empresa)+'\nhttps://finance.yahoo.com/quote/'+f'{args[0]}',parse_mode=ParseMode.MARKDOWN
        else:
            update.message.reply_text('Por favor utiliza:\n /alerta  empresa > ó < cantidad')
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
            bot.send_message(chatId,f'★★★Alerta★★★\n{Empresa} {modificador} {valor}\nValor actual: {vactual}')
            C.borrar(chatId,Id)
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
    dispatcher.add_handler(CommandHandler('menu_principal', comandos_comando))
    dispatcher.add_handler(CommandHandler('alerta',alerta_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('start', hola_comando))
    dispatcher.add_handler(CommandHandler('adios', adios_comando))
    dispatcher.add_handler(CommandHandler('cambio',cambio_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('valor', valor_comando, pass_args = True))
    dispatcher.add_handler(CommandHandler('debug', debug_comando))
    updater.start_polling(clean=True)
    j = updater.job_queue
    job_minute = j.run_repeating(alerta_hilo, interval=60, first=0)
    updater.idle()

if __name__ == '__main__':
    main(argv)
