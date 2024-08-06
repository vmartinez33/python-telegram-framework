from importlib import import_module

def include(arg, abspath=False):
    """Includes handlers defined in another module.
    
    Args:
        arg (str): Path to the handlers module. It can be relative to the directory configured for the modules in settings.py, or absolute from the root of the project.
        abspath (bool): If True, `arg` is considered an absolute path from the project root.

    Returns:
        list: List of handlers included from the specified module
    """
    try:
        if not abspath:
            #TODO (EXTRA): definir en settings.py la ruta relativa por defecto donde buscar los modulos (por ahora será dentro de /app)
            arg = 'app.'+arg
        handler_module = import_module(arg)
        handlers = getattr(handler_module, 'handlers')
    except ModuleNotFoundError:
        print(f"The module {arg} does not exist")
    except AttributeError:
        print(f"The module {arg} does not have a 'handlers' attribute")
    
    return handlers
