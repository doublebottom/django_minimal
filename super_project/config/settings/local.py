from .base import *

# custom settings

INSTALLED_APPS += [
    'super.names.apps.NamesConfig',
]

TEMPLATES[0]['DIRS'].append(BASE_DIR / 'templates')

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

