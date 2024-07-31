import os
import sys
import subprocess

from telegram_framework.management.utils import is_valid_python_version, copy_template


TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'templates', 'project_template')

def modify_pipfile(destination, python_version):    
    pipfile_path = os.path.join(destination, 'Pipfile')
    if os.path.exists(pipfile_path) and python_version:
        with open(pipfile_path, 'a') as file:
            file.write(f'\n[requires]\npython_version = "{python_version}"\n')

def startproject(project_name, python_version = None):
    if python_version and not is_valid_python_version(python_version):
        print("Error: Python version must be 3.8 or higher.")
        sys.exit(1)
    
    destination = os.path.join(os.getcwd(), project_name)
    copy_template(TEMPLATE_DIR, destination)
    if python_version:
        modify_pipfile(destination, python_version)
        
    print(f"Project '{project_name}' created successfully at {destination}\n")
    
    # Ask user if want to run "pipenv install" command 
    install_dependencies = input("Would you like to create a virtual environment and install project dependencies now? (y/n): ").strip().lower()
    if install_dependencies == 'y':
        try:
            subprocess.check_call(['pipenv', 'install'], cwd=destination)
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error installing dependecies:", e)
            sys.exit(1)

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'startproject':
        print("Usage: python-telegram-framework startproject <project_name> [python_version]")
        sys.exit(1)
    
    project_name = sys.argv[2]
    python_version = sys.argv[3] if len(sys.argv) > 3 else None    
    startproject(project_name, python_version)

if __name__ == "__main__":
    main()
