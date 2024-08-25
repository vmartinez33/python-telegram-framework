import os

from telegram_framework.conf import settings

def test_initialized_project(temporary_project):
    project_dir = temporary_project.get('project_dir', None)
    assert project_dir is not None
    
    # Check if app, manage, settings, handlers and callbacks files are present
    app_file = os.path.join(project_dir, 'app.py')
    manage_file = os.path.join(project_dir, 'manage.py')
    settings_file = os.path.join(project_dir, 'app', 'settings.py')
    handlers_file = os.path.join(project_dir, 'app', 'handlers.py')
    callbacks_file = os.path.join(project_dir, 'app', 'callbacks.py')
    assert (
        os.path.isfile(app_file) and 
        os.path.isfile(manage_file) and 
        os.path.isfile(settings_file) and
        os.path.isfile(handlers_file) and
        os.path.isfile(callbacks_file)
    )
    
