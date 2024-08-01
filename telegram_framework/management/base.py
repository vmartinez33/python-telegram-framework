import argparse
from abc import ABC, abstractmethod


class CommandError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
    
    def __str__(self):
        return f"CommandError: {self.message}"


class BaseCommand(ABC):
    @property
    @abstractmethod
    def help(self):
        pass
    
    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.help)
        self.add_arguments(self.parser)
        
    @abstractmethod
    def add_arguments(self, parser):
        pass
    
    @abstractmethod
    def handle(self, **options):
        pass
    
    def print_help(self):
        self.parser.print_help()    

    def execute(self, *args, **kwargs):
        try:
            options = self.parser.parse_args(args)
            self.handle(**vars(options))
        except CommandError as e:
            print(f"Error: {e}")
            self.print_help()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.print_help()
