# telegram_framework/management/commands/startproject.py

import os
import sys
import shutil

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

def startproject(project_name):
    destination = os.path.join(os.getcwd(), project_name)
    copy_template(TEMPLATE_DIR, destination)
    print(f"Project '{project_name}' created successfully at {destination}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != 'startproject':
        print("Usage: python-telegram-framework startproject <project_name>")
        sys.exit(1)
    
    project_name = sys.argv[2]
    startproject(project_name)

if __name__ == "__main__":
    main()
