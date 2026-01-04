"""
Admin configuration for the Blog application.

The admin interface allows site staff to manage categories and posts. Posts are
displayed with fields like title, category, status, and timestamps. Slug fields
are prepopulated for convenience.
"""

from __future__ import annotations

from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category."""

    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post."""

    list_display = ("title", "category", "status", "created_at", "updated_at")
    list_filter = ("status", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "created_at"
    ordering = ("status", "-created_at")