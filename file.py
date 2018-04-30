# coding utf-8

from telegram.ext import CommandHandler, Updater
from cambio import Bolsa
from Noticias import Noticias
import inspect
import datetime
from sys import argv

#TOKEN = ''
API1 = ''
API2 = ''
#devolver un hola al usuario
def hola_comando(bot, update):
    update.message.reply_text(
        'Hola {}, por ahora soporto /hola, /adios, /cambio moneda1 moneda2, /noticias, /valor empresa, /cambioayuda, /valorayuda, /noticiasayuda '.format(update.message.from_user.first_name))

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
        c = Bolsa(API2)
        update.message.reply_text(c.cambio(moneda1, moneda2))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /cambio moneda1 moneda2')

def cambioayuda_comando(bot, update,):
        update.message.reply_text('Los cambios aceptados son entre éste tipo de monedas: \n EUR-EURO  \n USD-DOLAR AMERICANO   JPY  \n CHF \n  AUD \n  CAD \n  NZD \n  GBP  \n SEK \n  NOK\n   MXN \n  TRY \n   ZAR \n  CNH \n  XAU \n  XAG \n  SGD \n  RUB \n  HKD \n  DKK \n  PLN \n  BTC - BitCoin \n ETH - Etherum \n LTC - LittleCoin \n XRP \n  DSH \n BCH\n')        

#noticias
def noticias_comando(bot, update, args):
    if len(args) == 1:
        #print('MAIN NOTICIAS')
        try:
            C = Noticias()
            valor = args[0]
            noticias = []
            noticias = C.rss(valor)
            for i in range(len(noticias)):
                #print(f'i: {i} {noticias[i]}')
                update.message.reply_text(f'{noticias[i]}')
            #chequeamos si está vacío
            if not noticias:
                update.message.reply_text('Comando erroneo, por favor utiliza:\n /noticias 1 ó 2')
        except Exception as ex:
            print(f'{datetime.datetime.now().time()}: {ex}')
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /noticias 1 ó 2')

#acción
def accion_comando(bot, update, args):
    if len(args) == 1:
        print('hello world')
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /accion empresa')


def main(args):
    with open('token1.txt') as f:
        global API1
        API1 = f.readline()
        print(f'API-1: {API1}')
    with open('token2.txt') as f:
        global API2
        API2 = f.readline()
        print(f'API-2: {API2}')
    updater = Updater(API1)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('noticias',noticias_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('hola', hola_comando))
    dispatcher.add_handler(CommandHandler('adios', adios_comando))
    dispatcher.add_handler(CommandHandler('cambio',cambio_comando,pass_args = True))
    dispatcher.add_handler(CommandHandler('cambioayuda',cambioayuda_comando))
    #dispatcher.add_handler(CommandHandler('accion', accion_comando, pass_args = True))
    updater.start_polling(clean=True)
    updater.idle()

if __name__ == '__main__':
    main(argv)