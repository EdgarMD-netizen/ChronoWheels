"""
Django settings for the ChronoWheels project.

This configuration is designed with security and flexibility in mind. It pulls
critical values such as the secret key and database connection parameters from
environment variables. If these values are not provided, the project falls
back to sensible defaults that allow the application to run in a development
environment. In production you should set ``DJANGO_DEBUG`` to ``False`` and
provide a strong ``DJANGO_SECRET_KEY`` along with MySQL connection details.
"""

from __future__ import annotations

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured  # type: ignore
import dj_database_url

def get_env(key: str, default: str | None = None) -> str:
    """Retrieve environment variables and optionally provide a default.

    If the environment variable is not defined and no default is provided,
    an ImproperlyConfigured error will be raised. This helps avoid launching
    the server with missing critical configuration such as the secret key.

    Args:
        key: Name of the environment variable.
        default: Fallback value if the environment variable is not set.

    Returns:
        The value of the environment variable or the provided default.
    """
    try:
        value = os.environ[key]
    except KeyError:
        if default is not None:
            return default
        raise ImproperlyConfigured(f"The {key} environment variable is not set.")
    return value


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env("DJANGO_SECRET_KEY", "unsafe-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env("DJANGO_DEBUG", "False").lower() == "true"

if not DEBUG and SECRET_KEY == "unsafe-secret-key":
    raise ImproperlyConfigured("DJANGO_SECRET_KEY must be set in production.")

ALLOWED_HOSTS_ENV = get_env("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,chronowheels.onrender.com").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_ENV if host.strip()]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apps
    "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "chronowheels_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chronowheels_project.wsgi.application"

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases


DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    # Fallback to SQLite or old logic
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 9},
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = "en-us"

# Set the timezone to the user's locale (America/Chicago)
TIME_ZONE = "America/Chicago"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/ref/settings/#static-files

STATIC_URL = "/static/"

# In production, STATIC_ROOT defines where collectstatic places files
STATIC_ROOT = BASE_DIR / "staticfiles"

# Additional directories that hold static files
STATICFILES_DIRS = [BASE_DIR / "static"]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security enhancements
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
X_FRAME_OPTIONS = "DENY"
SECURE_SSL_REDIRECT = not DEBUG  # redirect HTTP to HTTPS in production
