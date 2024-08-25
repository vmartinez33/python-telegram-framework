""" Global fixtures available for all test functions """

import os
import pytest
from telegram_framework.management import execute_from_command_line

@pytest.fixture(scope="session")
def temporary_project(tmp_path):
    """Fixture to initialize a project using the framework."""
    
    project_name = "test_project"
    
    # Change to temporary directory
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    try:
        # Create temporary project with "startproject" command
        execute_from_command_line(['python-telegram-framework', 'startproject', project_name])
        project_dir = os.path.join(tmp_path, project_name)
        
        # Check that the project was created successfully
        assert project_dir.exists()
        assert project_dir.is_dir()
        
        yield project_dir
        
    finally:
        # Return to the original working directory
        os.chdir(original_cwd)
