import os
import shutil
from abc import ABC, abstractmethod

from .base import BaseCommand, CommandError

class TemplateCommand(BaseCommand, ABC):
    @property
    @abstractmethod
    def template_directory(self):
        pass
    
    def __init__(self):
        super().__init__()
        
    def copy_template(template_dir, destination):
        if os.path.exists(destination):
            raise CommandError(f"The destination directory '{destination}' already exists.")
            
        os.makedirs(destination)
        
        for item in os.listdir(template_dir):
            src = os.path.join(template_dir, item)
            dst = os.path.join(destination, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
