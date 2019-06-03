import os
import sys

from decouple import config


# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATES = os.path.join(BASE_DIR, "templates")
SITE_STATIC = os.path.join(BASE_DIR, "static")
ROOT_URLCONF = "conf.urls"
WSGI_APPLICATION = "conf.wsgi.application"
SITE_ID = 1

# -----------------------------------------------------------------------------
# Time & Language
# -----------------------------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# Security and Users
# -----------------------------------------------------------------------------

SECRET_KEY = config("SECRET_KEY", default="$9597jcpibr3w!$(y^lm+77qp()*wc^ty%ak4v!g(@s%")
AUTH_USER_MODEL = "users.CustomUser"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------------------------------------------------------
# Applications configuration
# -----------------------------------------------------------------------------

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",

    # Third party
    "webpack_loader",
    "rest_framework",
    "robots",
    "cachalot",

    # Local apps
    "apps.users",
    "apps.blog",
    "apps.pages",
    "apps.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.processors.global_query",
            ]
        },
    }
]


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
}

# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [SITE_STATIC]
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
VENV_PATH = os.path.dirname(BASE_DIR)
MEDIA_ROOT = os.path.join(VENV_PATH, "media_root")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

VUE_FRONTEND_DIR = os.path.join(BASE_DIR, 'dashboard')
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dashboard/',  # must end with slash
        'STATS_FILE': os.path.join(VUE_FRONTEND_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.3,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# -----------------------------------------------------------------------------
# Django Debug Toolbar
# -----------------------------------------------------------------------------

TESTING_MODE = "test" in sys.argv
