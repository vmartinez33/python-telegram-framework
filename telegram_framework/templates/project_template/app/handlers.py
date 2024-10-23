from telegram.ext import filters, CommandHandler, MessageHandler

from .callbacks import cmd_start, cmd_help, msg_echo

handlers = [
    cmd_start,
    cmd_help,
    msg_echo,
]
