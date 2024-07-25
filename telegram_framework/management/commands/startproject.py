# telegram_framework/management/commands/startproject.py

import os
import sys
import shutil

from packaging.version import parse as parse_version

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'templates', 'project_template')

def copy_template(template_dir, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for item in os.listdir(template_dir):
        src = os.path.join(template_dir, item)
        dst = os.path.join(destination, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
            
def modify_pipfile(destination, python_version):    
    pipfile_path = os.path.join(destination, 'Pipfile')
    if os.path.exists(pipfile_path) and python_version:
        with open(pipfile_path, 'a') as file:
            file.write(f'\n[requires]\npython_version = "{python_version}"\n')        

def is_valid_python_version(version):
    return parse_version(version) >= parse_version("3.8")

def startproject(project_name, python_version = None):
    if python_version and not is_valid_python_version(python_version):
        print("Error: Python version must be 3.8 or higher.")
        sys.exit(1)
    
    destination = os.path.join(os.getcwd(), project_name)
    copy_template(TEMPLATE_DIR, destination)
    if python_version:
        modify_pipfile(destination, python_version)
    print(f"Project '{project_name}' created successfully at {destination}")

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'startproject':
        print("Usage: python-telegram-framework startproject <project_name> [python_version]")
        sys.exit(1)
    
    project_name = sys.argv[2]
    python_version = sys.argv[3] if len(sys.argv) > 3 else None    
    startproject(project_name, python_version)

if __name__ == "__main__":
    main()