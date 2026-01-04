#!/usr/bin/env python
"""
This script serves as the command‑line utility for the ChronoWheels project.

It provides access to various Django commands such as starting the development
server, migrating the database, and creating superusers. The settings module
for this project defaults to ``chronowheels_project.settings``. To override
this behaviour, set the ``DJANGO_SETTINGS_MODULE`` environment variable when
invoking this script.

The script intentionally avoids importing Django until necessary to prevent
unnecessary side effects. See the Django documentation for full usage
instructions: https://docs.djangoproject.com/en/stable/ref/django-admin/
"""
import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chronowheels_project.settings")
    try:
        from django.core.management import execute_from_command_line  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()