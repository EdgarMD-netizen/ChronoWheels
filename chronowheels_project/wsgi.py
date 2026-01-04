"""
WSGI config for the ChronoWheels project.

It exposes the WSGI callable as a module-level variable named ``application``.
This file is necessary for deploying the project on WSGI-capable web servers
such as Gunicorn or uWSGI.
"""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application  # type: ignore

# Use the project settings module by default
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chronowheels_project.settings")

application = get_wsgi_application()
