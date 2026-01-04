"""
URL patterns for the Blog app.

The blog exposes three core routes: the home page, category listing pages and
individual post pages. A namespace is defined to avoid collisions with other
applications.
"""

from __future__ import annotations

from django.urls import path

from . import views


app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_list, name="category"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
    path("privacy/", views.privacy_policy, name="privacy"),
]