from .base import *


# Disable debug mode

DEBUG = False
TEMPLATE_DEBUG = False
THUMBNAIL_DEBUG = False

ALLOWED_HOSTS = ['.cccolomboturca.co','.cccolomboturca.co.']

ADMINS = (
    ('ColomboTurca', 'oficial@cccolomboturca.co'),
)

MANAGERS = ADMINS

#Server's Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cccolomboturca',
        'USER': 'colomboturca',
        'PASSWORD': 'colomboturca',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

#Static Files

MEDIA_ROOT = '/home/salahaddinal/webapps/cccturca_static/media'
STATIC_ROOT = '/home/salahaddinal/webapps/cccturca_static/static'
STATICFILES_DIRS = (join(dirname(PROJECT_ROOT), "ccct", "core", "static", "ccct"),)
#join(PROJECT_ROOT, '/core/static/anadolu/')

MEDIA_URL = '/static/media/'
STATIC_URL = '/static/static/'

# Compress static files offline
# http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE

COMPRESS_OFFLINE = True


# Send notification emails as a background task using Celery,
# to prevent this from blocking web server threads
# (requires the django-celery package):
# http://celery.readthedocs.org/en/latest/configuration.html

# import djcelery
#
# djcelery.setup_loader()
#
# CELERY_SEND_TASK_ERROR_EMAILS = True
# BROKER_URL = 'redis://'

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Use Redis as the cache backend for extra performance
# (requires the django-redis-cache package):
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#cache

# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'KEY_PREFIX': 'ccct',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
#         }
#     }
# }

#Search
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'URLS': ['http://localhost:9200'],
        'INDEX': 'anadolu',
        'TIMEOUT': 5,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Web Mail Servers
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'anadoludkmco'
EMAIL_HOST_PASSWORD = 'Hikmetadkm'
DEFAULT_FROM_EMAIL = 'oficial@anadoludkm.co'
SERVER_EMAIL = 'oficial@anadoludkm.co'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
