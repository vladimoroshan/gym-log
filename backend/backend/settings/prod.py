import os
import dj_database_url
from backend.settings.base import *
from backend.common.utils import get_env_var

DEBUG = False

INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASE_URL = get_env_var('DATABASE_URL')
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=True)

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "frontend", "build")]
WHITENOISE_ROOT = os.path.join(BASE_DIR, "frontend", "build", "root")

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend", "build", "static")]
