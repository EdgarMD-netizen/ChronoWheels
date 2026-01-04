"""
ASGI config for the ChronoWheels project.

This module exposes the ASGI callable as a module-level variable named
``application``. Django uses this file to serve the project using ASGI
compatible servers. For more information on ASGI, see:
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

from __future__ import annotations

import os

from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chronowheels_project.settings")

application = get_asgi_application()
