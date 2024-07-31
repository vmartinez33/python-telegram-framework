# telegram_framework/management/commands/startproject.py

import os
import sys
import shutil
import subprocess

# TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'templates', 'module_template')

# def copy_template(template_dir, destination):
#     if not os.path.exists(destination):
#         os.makedirs(destination)
    
#     for item in os.listdir(template_dir):
#         src = os.path.join(template_dir, item)
#         dst = os.path.join(destination, item)
#         if os.path.isdir(src):
#             shutil.copytree(src, dst)
#         else:
#             shutil.copy2(src, dst)
                

# def createmodule(project_name, python_version = None):
#     destination = os.path.join(os.getcwd(), project_name)
#     copy_template(TEMPLATE_DIR, destination)
        
#     print(f"Project '{project_name}' created successfully at {destination}\n")
    
#     # Ask user if want to run "pipenv install" command 
#     install_dependencies = input("Would you like to create a virtual environment and install project dependencies now? (y/n): ").strip().lower()
#     if install_dependencies == 'y':
#         try:
#             subprocess.check_call(['pipenv', 'install'], cwd=destination)
#             print("Dependencies installed successfully.")
#         except subprocess.CalledProcessError as e:
#             print("Error installing dependecies:", e)
#             sys.exit(1)

# def main():
#     if len(sys.argv) < 3 or sys.argv[1] != 'startproject':
#         print("Usage: python manage.py createmodule <module_name>")
#         sys.exit(1)
    
#     project_name = sys.argv[2]
#     python_version = sys.argv[3] if len(sys.argv) > 3 else None    
#     createmodule(project_name, python_version)

# if __name__ == "__main__":
#     main()
