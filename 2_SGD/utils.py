import importlib
import os
import sys

# __file__ is a variable that contains the path to the module that is currently being imported. 
# E.g.:
# os.path.realpath(__file__)  == /Users/shamsi/Desktop/dlpython/source/Round2/utils.py
# dir_path == /Users/shamsi/Desktop/dlpython/source/Round2
dir_path = os.path.dirname(os.path.realpath(__file__))


# path to utils dir with __init__.py 
# __init__.py imports load_styles, TestResult etc.
module_path = os.path.join(dir_path, '..', '..', '..', 'coursedata')
#module_path = os.path.join(dir_path,'..', '..', 'data') # /Users/shamsi/Desktop/dlpython/source/Round2/../../data


if module_path not in sys.path:
    sys.path.insert(0, module_path)

# Temporarily hijack __file__ to avoid adding names at module scope;  i.e. we are resuing var name __file__
# __file__ will be overwritten again during the reload() call.

# {'sys': <module 'sys' (built-in)>, 
#. 'importlib': <module 'importlib' from '/Users/shamsi/anaconda3/envs/dlaalto/lib/python3.7/importlib/__init__.py'>}
__file__ = {'sys': sys, 'importlib': importlib}


# delete objects (vals are still stored in __file__ dict)
del importlib
del os
del sys

# __name__ is a string containing the module name
# load utils (dir) from inserted path
__file__['importlib'].reload(__file__['sys'].modules[__name__])



