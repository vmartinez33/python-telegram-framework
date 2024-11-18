import os
import sys

from telegram_framework.conf import settings
from telegram_framework.management.base import CommandError
from telegram_framework.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = "Create a new module within the project"
    template_name = "module_template"
    
    def __init__(self, argv):
        super().__init__(argv)

    def handle(self, **options):
        name = options.get('name')

        base_directory = os.path.join(os.getcwd(), *settings.MODULES_DIR.split('.'))
        destination = os.path.join(base_directory, name)
        self.copy_template(destination)
        
        print(f"Module '{name}' created successfully at {destination}\n")
