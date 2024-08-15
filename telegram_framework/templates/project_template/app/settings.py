import logging

# Project configuration
DEBUG = True

# Telegram Bot configuration
TELEGRAM_BOT_TOKEN = '6123421745:AAFRDsCkCOMRneXpc7rMwnQkqdwXieXIYIY'

# Logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
