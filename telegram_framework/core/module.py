from telegram_framework.handlers.decorators import HandlerDecorators


class Module(HandlerDecorators):
    def __init__(self, name: str, import_name: str) -> None:
        self.name = name
        self.import_name = import_name
