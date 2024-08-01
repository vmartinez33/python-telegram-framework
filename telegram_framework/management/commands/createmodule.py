import os
import sys
import subprocess

from telegram_framework.management.base import CommandError
from telegram_framework.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = "Create a new module within the project"
    template_name = "module_template"
    
    def __init__(self, argv):
        super().__init__(argv)
        
    def handle(self, **options):
        name = options.get('name')
        #TODO (EXTRA): definir en settings.py la ruta relativa por defecto donde crear los modulos dentro del proyecto (por ahora será dentro de /app)
        destination = os.path.join(os.getcwd(), 'app', name)
        self.copy_template(destination)
        print(f"Module '{name}' created successfully at {destination}\n")
