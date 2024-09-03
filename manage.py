#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""

    # Determine the environment
    env = os.getenv('DJANGO_ENV', 'development')  # Default to development
    # Set the settings module
    if env == 'development':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devjobs_portal.settings.development')
    elif env == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devjobs_portal.settings.production')
    else:
        raise ValueError(f"Unknown DJANGO_ENV: {env}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
