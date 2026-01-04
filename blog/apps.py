"""
App configuration for the blog app.

This configuration sets a verbose name for the admin interface and ensures
Django picks up this app when auto‑discovering applications.
"""

from __future__ import annotations

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configuration for the Blog application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = "ChronoWheels Blog"