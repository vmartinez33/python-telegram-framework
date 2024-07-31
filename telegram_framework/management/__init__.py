import sys

from telegram_framework.management.commands import startproject # Esto es temporal

def execute_from_command_line(argv=None):
    argv = argv or sys.argv
    print(argv)
    
    if argv[1] == 'startproject':
        startproject.main()
