from importlib import import_module

def include(arg):
    """ Function that includes the handlers of one file in another.
    It is assumed that 'arg' indicates the exact path from the project root. Ex. 'app.module_1.handlers'.
    It returns a list of handlers for the given file (arg), so splat operator needs to be used: '*include()'.
    """
    try:
        handler_module = import_module(arg)
        handlers = getattr(handler_module, 'handlers')
    except ModuleNotFoundError:
        print(f"The module {arg} does not exist")
    except AttributeError:
        print(f"The module {arg} does not have a 'handlers' attribute")
    
    return handlers
