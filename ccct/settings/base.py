"""
Django settings for ccct project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from os.path import abspath, dirname, join

# Absolute filesystem path to the Django project directory:
PROJECT_ROOT = dirname(dirname(dirname(abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4+%@$v&8b@j+d%^!yts*hag!t(%rzen%ai=6sbbay+y#&901j='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = []

#TCP definition
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'core.context_processors.countrytimes',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

# Application definition

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'compressor',
    'taggit',
    'modelcluster',

    'django_extensions',
    'embed_video',
    'robots',
    'smart_selects',
    'sorl.thumbnail',

    'affiliates',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.wagtailsitemaps',

    'core',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'ccct.urls'
WSGI_APPLICATION = 'ccct.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# SQLite (simplest install)
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': join(PROJECT_ROOT, 'db.sqlite3'),
#    }
#}

# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql development headers)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ccct',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': '',  # Set to empty string for localhost.
#         'PORT': '',  # Set to empty string for default.
#         'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'    #Por defecto es 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = join(PROJECT_ROOT, 'static')
#STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

#MEDIA_ROOT = join(PROJECT_ROOT, 'media')
#MEDIA_URL = '/media/'


# Django compressor settings
# http://django-compressor.readthedocs.org/en/latest/settings/

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Wagtail settings

EMAIL_SUBJECT_PREFIX = '[Cámara de Comercio Colombo Turca]'
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'oficial@cccolomboturca.co'

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "Cámara de Comercio Colombo Turca"

WAGTAILSITEMAPS_CACHE_TIMEOUT = 10

# Override the search results template for wagtailsearch
#WAGTAILSEARCH_RESULTS_TEMPLATE = 'search_results.html'

# Use Elasticsearch as the search backend for extra performance and better search results:
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#search
# http://wagtail.readthedocs.org/en/latest/core_components/search/backends.html#elasticsearch-backend
#
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
#         'INDEX': 'ccct',
#     },
# }


# Whether to use face/feature detection to improve image cropping - requires OpenCV
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
    'embed_video.backends.SoundCloudBackend',
)

EMBED_VIDEO_TIMEOUT = (10)

#Robots
ROBOTS_CACHE_TIMEOUT = 60*60*24
ROBOTS_SITEMAP_URLS = [
    '',
]

#Suit customization
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Cámara de Comercio Colombi Turca',
    'HEADER_DATE_FORMAT': 'l j \d\e F \d\e Y', #'l, j. F Y',
    'HEADER_TIME_FORMAT': 'h:i a',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    #'SEARCH_URL': '/admin/auth/user/',
    'SEARCH_URL': '/admin/',
    'MENU': (
        'auth',
        '-',
        'sites',
        'robots',
        '-',
        {'app': 'affiliates', 'label': 'Afiliaciones'},
        '-',
        {'app': 'wagtaildocs', 'label': 'Documentos'},
        {'app': 'wagtailcore', 'label': 'Núcleo'},
        {'app': 'wagtailimages', 'label': 'Imágenes'},
        '-',
        {'app': 'taggit', 'label': 'Etiquetador'},

    ),
    'MENU_ICONS': {
        'affiliates': 'icon-list-alt',
        'auth': 'icon-lock',
        'robots': 'icon-qrcode',
        'sites': 'icon-leaf',
        'taggit': 'icon-tag',
        'wagtaildocs': 'icon-file',
        'wagtailcore': 'icon-book',
        'wagtailimages': 'icon-camera'
    },
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    'LIST_PER_PAGE': 20
}