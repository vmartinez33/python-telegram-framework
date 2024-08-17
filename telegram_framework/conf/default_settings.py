import logging

# Project configuration
DEBUG = False

MODULES_DIR = 'app.modules'
HANDLERS_MODULE = 'app.handlers'

# Webhook configuration
USE_WEBHOOK = False

WEBHOOK_LISTEN = "127.0.0.1"
WEBHOOK_PORT = 80
WEBHOOK_URL = "http://localhost/telegram"
WEBHOOK_IP_ADDRESS = None
WEBHOOK_SECRET_TOKEN = None
WEBHOOK_CERT = None
WEBHOOK_SSL_KEY = None

# Telegram Bot configuration
TELEGRAM_BOT_TOKEN = ''

# Logging configuration
LOGGING_LEVEL = logging.INFO # With DEGUG enabled, level is always DEBUG
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
