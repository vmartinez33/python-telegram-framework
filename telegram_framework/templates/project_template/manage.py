"""Command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    #TODO: ver cómo manejar los settigns, y dependiendo de eso, esto tendrá o no sentido
    # os.environ.setdefault('TELEGRAM_SETTINGS_MODULE', 'settings')
    
    try:
        from telegram_framework.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Telegram Framework. Did you "
            "forget to activate a virtual environment and install all dependencies?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
