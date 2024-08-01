import sys
import importlib

from telegram_framework.management.base import CommandError

def execute_from_command_line(argv=None):
    argv = argv or sys.argv
    print(argv)

    if len(argv) < 2:
        print("Please provide a command.")
        return

    command_name = argv[1]
    try:
        module = importlib.import_module(f'commands.{command_name}')
        command = module.Command()
        command.execute(*argv[2:])
    except ModuleNotFoundError:
        print(f"Command '{command_name}' could not be found.")
    except AttributeError:
        print(f"The module '{command_name}' does not have a 'Command' class.")
    except CommandError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
