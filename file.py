# coding utf-8

from telegram.ext import CommandHandler, Updater
from cambio import Bolsa
from Mercado import Accion
from Noticias import Noticias
import inspect
import datetime
from sys import argv
import pandas as pd


#devolver un hola al usuario
def hola_comando(bot, update):
    update.message.reply_text(
        'Hola {}, por ahora soporto:\n /hola \n /adios, \n/cambio moneda1 moneda2 \n /noticias \n /valor empresa \n /cambioayuda \n /valorayuda \n /noticiasayuda '.format(update.message.from_user.first_name))

#devolver un adios al usuario
def adios_comando(bot, update):
    update.message.reply_text(
        'Adios {}'.format(update.message.from_user.first_name))

#devolver cambio al usuario
def cambio_comando(bot, update, args):
    if len(args) == 2:
        moneda1, moneda2 = args
        moneda1 = moneda1.upper()
        moneda2 = moneda2.upper()
        C = Bolsa()
        update.message.reply_text(C.cambio(moneda1, moneda2))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /cambio moneda1 moneda2')

def cambioayuda_comando(bot, update,):
        update.message.reply_text('Los cambios aceptados son entre éste tipo de monedas: \n EUR-EURO  \n USD-DOLAR AMERICANO   JPY  \n CHF \n  AUD \n  CAD \n  NZD \n  GBP  \n SEK \n  NOK\n   MXN \n  TRY \n   ZAR \n  CNH \n  XAU \n  XAG \n  SGD \n  RUB \n  HKD \n  DKK \n  PLN \n  BTC - BitCoin \n ETH - Etherum \n LTC - LittleCoin \n XRP \n  DSH \n BCH\n')        

#noticias
def noticias_comando(bot, update, args):
    if len(args) == 1:
        #print('MAIN NOTICIAS')
        try:
            print(f'args[0] -> {args[0]}')
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
def accion_comando(bot, update, args):
    if len(args) == 1:
        C = Accion()
        #print(C.valor(args[0]))
        update.message.reply_text(C.valor(args[0]))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')


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
    dispatcher.add_handler(CommandHandler('start', hola_comando))
    dispatcher.add_handler(CommandHandler('adios', adios_comando))
    dispatcher.add_handler(CommandHandler('cambio',cambio_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('cambioayuda',cambioayuda_comando))
    dispatcher.add_handler(CommandHandler('accion', accion_comando, pass_args = True))
    updater.start_polling(clean=True)
    updater.idle()

if __name__ == '__main__':
    main(argv)