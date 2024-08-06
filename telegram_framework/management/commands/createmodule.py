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
        
    def ask_include_handlers(self, module_name):
        include_handlers = input("Do you want to include the handlers of this new module in the app handlers? (y/n):").strip().lower()
        if include_handlers == "y":
            app_handlers_path = os.path.join('app', 'handlers.py')
            module_import = f"*include('{module_name}.handlers'),\n"
            
            try:
                with open(app_handlers_path, 'r') as f:
                    content = f.readlines()
            except FileNotFoundError:
                print(f"The file '{app_handlers_path}' does not exist.")
                sys.exit(1)
            
            try: 
                with open(app_handlers_path, 'w') as f:
                    for line in content:
                        f.write(line)
                        if line.strip().startswith("handlers = ["):
                            f.write(f"\t{module_import}")
                
                print(f"Handlers of module '{module_name}' included in app handlers successfully.")
                reverse = input("\nDo you want to reverse the action? (y/n):").strip().lower()
                if reverse == "y":
                    with open(app_handlers_path, 'w') as f:
                        f.writelines(content)
                    print("Action successfully reversed.")
            except Exception as e:
                print(f"Error while including handlers: {e}")
                with open(app_handlers_path, 'w') as f:
                    f.writelines(content)
                sys.exit(1)

    def handle(self, **options):
        name = options.get('name')
        #TODO (EXTRA): definir en settings.py la ruta relativa por defecto donde crear los modulos dentro del proyecto (por ahora será dentro de /app)
        destination = os.path.join(os.getcwd(), 'app', name)
        self.copy_template(destination)
        
        print(f"Module '{name}' created successfully at {destination}\n")
        
        self.ask_include_handlers(name)
        
