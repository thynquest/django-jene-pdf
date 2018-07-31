#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jenesample.settings")
    #root_path = os.path.abspath(os.path.join(__file__, '..', '..'))
    #print("root path => {}".format(root_path))
    #lib_path = os.path.join(root_path, 'jeneprocessor')
    #print("lib path => {}".format(lib_path))
    #sys.path.insert(0, lib_path)4
    sys.path.append('..')
    # print("sys path => {}".format(sys.path))
    #sys.path.append('...')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
