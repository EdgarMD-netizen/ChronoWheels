"""
Database models for the ChronoWheels blog.

The application defines two simple models: ``Category`` and ``Post``. A
``Category`` represents a thematic grouping of blog posts (e.g. history,
safety, materials, hybrid). Each ``Post`` belongs to exactly one category and
contains rich text content. Posts may be drafted or published. Slugs are used
for human‑readable URLs.
"""

from __future__ import annotations

from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Represents a logical grouping of posts."""

    name: str = models.CharField(max_length=100, unique=True)
    slug: str = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        """Return the URL for listing posts in this category."""
        return reverse("blog:category", kwargs={"slug": self.slug})


class Post(models.Model):
    """Represents a blog post entry."""

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title: str = models.CharField(max_length=200)
    slug: str = models.SlugField(max_length=220, unique=True)
    category: Category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    excerpt: str = models.TextField(blank=True, help_text="Short summary shown on listing pages.")
    content: str = models.TextField(help_text="Full blog post content in HTML or Markdown.")
    status: str = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        """Return the URL for the detail view of this post."""
        return reverse("blog:post_detail", kwargs={"slug": self.slug})