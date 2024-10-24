from typing import Optional

from telegram.ext import filters, CommandHandler, MessageHandler
from telegram.ext.filters import BaseFilter


def command(command_name: str, filters: Optional[BaseFilter] = None, block: bool = True, has_args: Optional[bool | int] = None) -> CommandHandler:
    """Decorator to return a CommandHandler for a callback function."""
    def decorator(func):
        return CommandHandler(command_name, func, filters, block, has_args)
    return decorator


def message(filters: Optional[BaseFilter] = filters.TEXT & ~filters.COMMAND, block: bool = True) -> CommandHandler:
    """Decorator to return a MessageHandler for a callback function."""
    def decorator(func):
        return MessageHandler(filters, func, block)
    return decorator

