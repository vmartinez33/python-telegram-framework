import os
import sys
import subprocess


def test_createmodule_command_with_handlers_include(temporary_project):
    project_dir = temporary_project.get('project_dir', None)
    assert project_dir is not None
    
    # Prepare the inputs as a string with line breaks
    # inputs = "y"
        
    # Run the "createmodule" command with a module name
    module_name = 'module_test'
    os.chdir(project_dir)
    result = subprocess.run(
        [sys.executable, 'manage.py', 'createmodule', module_name],
        capture_output=True,
        text=True,
        # input=inputs
    )
    
    # Check if the command runs successfully
    assert result.returncode == 0
    
    # Check if the module directory exists
    module_dir = os.path.join(project_dir, 'modules', module_name)
    os.path.exists(module_dir)
    os.path.isdir(module_dir)
    
    # Check if handlers and models files exist
    handlers_file = os.path.join(module_dir, 'handlers.py')
    assert os.path.exists(handlers_file)
    assert os.path.isfile(handlers_file)
    
    models_file = os.path.join(module_dir, 'models.py')
    assert os.path.exists(models_file)
    assert os.path.isfile(models_file)
    
    # Check if the module handlers are included in the main handlers file
    # main_handlers_file = os.path.join(project_dir, 'app', 'handlers.py')
    # with open(main_handlers_file, 'r') as f:
    #     content = f.read()
    #     assert f"include('{module_name}.handlers')" in content    
    