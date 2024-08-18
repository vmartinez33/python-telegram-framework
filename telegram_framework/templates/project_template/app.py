import os
import logging
import importlib

from telegram.ext import Application
from pyngrok import ngrok, conf

from telegram_framework.conf.utils import initialize_settings
from telegram_framework.conf import settings

initialize_settings(__file__)

logging.basicConfig(
    format=settings.LOGGING_FORMAT,
    level=logging.DEBUG if settings.DEBUG else settings.LOGGING_LEVEL
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Set the handlers for the specified module in the settings.py file ('app.handlers' by default).
    handlers_module = importlib.import_module(settings.HANDLERS_MODULE)
    handlers = getattr(handlers_module, 'handlers')
    application.add_handlers(handlers=handlers)

    # Run the bot until the user presses Ctrl-C
    if settings.USE_WEBHOOK:
        # ngrok configuration
        if settings.USE_NGROK:
            conf.get_default().config_path = "./config_ngrok.yml"
            conf.get_default().region = settings.NGROK_REGION
            ngrok.set_auth_token(settings.NGROK_TOKEN)
            ngrok_tunel = ngrok.connect(settings.WEBHOOK_PORT, bind_tls=True)
            ngrok_url = ngrok_tunel.public_url
        
        # Webhook setup
        application.run_webhook(
            listen=settings.WEBHOOK_LISTEN,
            port=settings.WEBHOOK_PORT,
            url_path=settings.WEBHOOK_URL_PATH,
            webhook_url=ngrok_url if settings.USE_NGROK else settings.WEBHOOK_URL,
            ip_address=settings.WEBHOOK_IP_ADDRESS,
            secret_token=settings.WEBHOOK_SECRET_TOKEN,
            cert=settings.WEBHOOK_CERT,
            key=settings.WEBHOOK_SSL_KEY,
        )
    else:
        # Polling setup
        application.run_polling()


if __name__ == "__main__":
    main()
