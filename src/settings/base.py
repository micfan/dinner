"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG



SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'zh-cn'
LANGUAGES = (
    ('en', 'English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dd24gm48g6m(jfy-@fir0t#h9tih33(2_^%^9w1_^=5!&0qu6q'

INSTALLED_APPS = (
    'public',
    'dinner',
    'apps',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))
# Assume that the presence of 'activate_this.py' in the python bin/
# directory means that we're running in a virtual environment.
if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    # We're running with a virtualenv python executable.
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    # We're running in [virtualenv_root]/src/[project_name].
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    # Set the variable root to a path in the project which is
    # ignored by the repository.
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================
APPEND_SLASH = True
ROOT_URLCONF = 'root_urls'

AUTH_USER_MODEL = 'public.User'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'


STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_FINDERS = (
  "django.contrib.staticfiles.finders.FileSystemFinder",
  "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

# STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

# TEMPLATE_LOADERS = (
#     'django.template.loaders.app_directories.Loader',
# )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # ('django.template.loaders.cached.Loader', (
    #     'django.template.loaders.filesystem.Loader',
    #     'django.template.loaders.app_directories.Loader',
    # )),
)

TEMPLATE_CONTEXT_PROCESSORS += (
  'django.core.context_processors.csrf',
  'django.contrib.messages.context_processors.messages',
  'django.core.context_processors.static',
  'django.core.context_processors.request',
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
  # 'django.contrib.auth.backends.ModelBackend',
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================
