"""
Settings for this telegram framework project.

For the full list of settings and their values, see:
"""

# Project configuration
DEBUG = True

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
TELEGRAM_BOT_TOKEN = 'MY BOT TOKEN'
