from telegram.ext import filters, CommandHandler, MessageHandler

from app.base import _start, _help, _echo

#TODO: funcionalidad para poder importar aqui los handlers de otros modulos
handlers = [
    CommandHandler('start', _start),
    CommandHandler('help', _help),
    MessageHandler(filters.TEXT & ~filters.COMMAND, _echo),
]
