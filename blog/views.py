"""
Views for the ChronoWheels blog.

This module defines simple function‑based views to render the home page, list
posts by category, and display individual posts. All views automatically
provide a list of categories to the template context so that navigation can be
displayed consistently across the site.
"""

from __future__ import annotations

from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def _common_context() -> dict[str, object]:
    """Return context data shared across multiple views."""
    from django.utils import timezone
    return {
        "categories": Category.objects.all().order_by("name"),
        # Provide the current timestamp so templates can display the year.
        "now": timezone.now(),
    }


def home(request):
    """Render the home page showing all published posts."""
    post = Post.objects.order_by("-created_at").first()

    context = {
        "post": post,
        **_common_context(),
    }
    
    if not post:
        return render(request, "blog/empty.html", context)
    
    return render(request, "blog/home.html", context)


def category_list(request, slug: str):
    """Render a page listing published posts within a specific category."""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status="published")
    context = {
        "category": category,
        "posts": posts,
        **_common_context(),
    }
    return render(request, "blog/section_list.html", context)


def post_detail(request, slug: str):
    """Render a page showing the details of a single post."""
    post = get_object_or_404(Post, slug=slug, status="published")
    context = {
        "post": post,
        **_common_context(),
    }
    return render(request, "blog/post_detail.html", context)


def privacy_policy(request):
    """Render a simple privacy policy page required by AdSense."""
    context = {
        **_common_context(),
    }
    return render(request, "blog/privacy.html", context)