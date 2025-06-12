#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    
    # Establece el módulo de settings por defecto para desarrollo
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educablog.settings.development')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # Manejo especial para el comando test
    is_testing = 'test' in sys.argv
    if is_testing:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'webescuela.settings.testing'

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()