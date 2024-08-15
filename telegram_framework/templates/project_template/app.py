import os
import logging

from telegram.ext import Application

from telegram_framework.conf import settings

from app.handlers import handlers

logging.basicConfig(
    format=settings.LOGGING_FORMAT,
    level=logging.DEBUG if settings.DEBUG else settings.LOGGING_LEVEL
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    # Set the handlers defined in the handlers.py file
    application.add_handlers(handlers=handlers)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    
    #TODO: Implementar flexibilidad para usar polling o webhooks
    # if USE_WEBHOOK:
    #     # Webhook setup
    #     application.run_webhook(
    #         listen="0.0.0.0",
    #         port=PORT,
    #         url_path=WEBHOOK_URL.split('/')[-1],
    #         webhook_url=WEBHOOK_URL
    #     )
    # else:
    #     # Polling setup
    #     application.run_polling()


if __name__ == "__main__":
    main()
