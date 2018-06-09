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
        'Hola {}, por ahora soporto:\n /hola \n /adios, \n/cambio \n /noticias \n/valor empresa \n/alerta'.format(f'@{update.message.from_user.username}'))

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
            #print(f'file: noticias_comando -> {datetime.datetime.now().time()}: {ex}')
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
            #print(f'file: noticias_comando -> {datetime.datetime.now().time()}: {ex}')

#acción
def valor_comando(bot, update, args):
    if len(args) == 1:
        C = Accion()
        #print(C.valor(args[0]))
        update.message.reply_text(C.valor(args[0]))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')

def alerta_comando(bot, update, args):
    update.message.reply_text('en contrucción')
    Log = Syslog()
    error = 'Comando erroneo, por favor utiliza:\n /alerta empresa < cantidad -> para crear una alerta \n /alerta lista -> para listar tus alertas \n /alerta borrar todas -> para borrar todas tus alertas \n /alerta borrar empresa < 1000 -> borra esa alerta'
    if len(args) == 0:
        Log.errorlog('file -> alerta_comando longitud comandos 0 {error}')
        update.message.reply_text(error)
    elif len(args) == 1:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')
    elif len(args) == 2:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')
    elif len(args) == 3:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')
    elif len(args) == 4:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')
    else:
        Log.errorlog('file -> alerta_comando {error}')
        update.message.reply_text(error)

def alerta_hilo(bot, job):
    Log = Syslog()
    #tenemos que buscar tareas pendientes de hacer
    if True:
        Log.log('comprobando hilo')
        print('comprobando hilo')
    else:
        print('no hagas nada')

def main(args):
    API1 = ''
    with open('./token1.txt', 'rU') as f:
        API1 = f.readline()
        f.close()
    #print(f'API-1->{API1}')
    updater = Updater(API1)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('noticias',noticias_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('hola', hola_comando))
    dispatcher.add_handler(CommandHandler('alerta', hola_comando))
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