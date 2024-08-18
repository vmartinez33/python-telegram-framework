import os
import importlib

from telegram.ext import Application
from pyngrok import ngrok, conf

from telegram_framework.conf import settings


class BotRunner:
    def __init__(self, bot=None, updater=None, context_type=None):
        application = Application.builder()
        
        if bot is not None:
            application = application.bot(bot)
        if updater is not None:
            application = application.updater(updater)
        if context_type is not None:
            application = application.context_types(context_type)
        
        self.application = application.token(settings.TELEGRAM_BOT_TOKEN).build()
        self.run_params = {}
        
    def set_run_params(self, **kwargs):
        self.run_params = kwargs
        
    def _get_handlers(self):
        try:
            handlers_module = importlib.import_module(settings.HANDLERS_MODULE)
        except ImportError:
            print("The handlers module could not be imported. Is the module correctly indicated in the settings.py file?")
            return
        
        handlers = getattr(handlers_module, 'handlers', None)
        if handlers is None:
            print("The handlers module does not contain any handlers. Check the module and its structure.")
            return
        
        return handlers
    
    def _configure_ngrok_and_get_url(self):
        try:
            conf.get_default().config_path = os.path.join(settings.BASE_DIR, 'config_ngrok.yml')
            conf.get_default().region = settings.NGROK_REGION
            ngrok.set_auth_token(settings.NGROK_TOKEN)
            ngrok_tunel = ngrok.connect(settings.WEBHOOK_PORT, bind_tls=True)
            ngrok_url = ngrok_tunel.public_url
        except Exception as e:
            print(f"Error while setting up ngrok: {e}")
            return
        
        return ngrok_url
 
    def run(self):
        # Set the handlers for the specified module in the settings.py file ('app.handlers' by default).
        handlers = self._get_handlers()
        self.application.add_handlers(handlers=handlers)
        
        if settings.USE_WEBHOOK:
            # ngrok configuration
            if settings.USE_NGROK:
                ngrok_url = self._configure_ngrok_and_get_url()
            
            # Webhook setup
            self.application.run_webhook(
                listen=settings.WEBHOOK_LISTEN,
                port=settings.WEBHOOK_PORT,
                url_path=settings.WEBHOOK_URL_PATH if settings.WEBHOOK_URL_PATH is not None else "",
                webhook_url=ngrok_url if settings.USE_NGROK else settings.WEBHOOK_URL,
                ip_address=settings.WEBHOOK_IP_ADDRESS,
                secret_token=settings.WEBHOOK_SECRET_TOKEN,
                cert=settings.WEBHOOK_CERT,
                key=settings.WEBHOOK_SSL_KEY,
                **self.run_params
            )
        else:
            # Polling setup
            self.application.run_polling(**self.run_params)