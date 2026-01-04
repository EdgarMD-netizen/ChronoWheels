"""
URL configuration for the ChronoWheels project.

This module defines the URL patterns that route incoming HTTP requests to
appropriate Django views. The project delegates most of the routing to the
``blog`` application while also exposing the Django admin interface. The admin
interface should remain accessible only to trusted staff and is protected by
default Django authentication.
"""

from __future__ import annotations

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
]
