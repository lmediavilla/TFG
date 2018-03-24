# coding utf-8

import logging
#from telegram.error import NetworkError, Unauthorized
from telegram.ext import CommandHandler, Updater
from cambio import Bolsa
import inspect
from sys import argv

#TOKEN = ''

#devolver un hola al usuario
def hola_comando(bot, update):
    update.message.reply_text(
        'Hola {}'.format(update.message.from_user.first_name))

#devolver un adios al usuario
def adios_comando(bot, update):
    update.message.reply_text(
        'Adios {}'.format(update.message.from_user.first_name))

#devolver cambio al usuario
def cambio_comando(bot, update, args):
    if len(args) == 2:
        moneda1, moneda2 = args
        #debug
        #print(f'{args[0]} y {args[1]}')
        c = Bolsa()
        update.message.reply_text(c.cambio(moneda1, moneda2))
    else:
        update.message.reply_text('Comando erroneo, por favor utiliza:\n /cambio moneda1 moneda2')

def main(args):
    updater = Updater(argv[1])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('hola', hola_comando))
    dispatcher.add_handler(CommandHandler('adios', adios_comando))
    dispatcher.add_handler(CommandHandler('cambio',cambio_comando,pass_args = True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main(argv)