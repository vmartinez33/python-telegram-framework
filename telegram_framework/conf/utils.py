import os
import sys

def initialize_settings(path = __file__, project_module = 'app.settings'):
    os.environ.setdefault('TELEGRAM_SETTINGS_MODULE', project_module)
    file_dir = os.path.abspath(os.path.dirname(path))
    if file_dir not in sys.path:
        sys.path.insert(0, file_dir)
