DEBUG = True
#SECRET_KEY = 'not a very secret key'
ADMINS = (
)
#ALLOWED_HOSTS = ["*"]

STATIC_ROOT = '/local/grader/static/'
MEDIA_ROOT = '/local/grader/media/'
SUBMISSION_PATH = '/local/grader/uploads'
PERSONALIZED_CONTENT_PATH = '/local/grader/ex-meta'
STATIC_URL_HOST_INJECT = 'http://localhost:8080'

CONTAINER_MODE = True
CONTAINER_SCRIPT = '/srv/docker-compose-run.sh'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/local/grader/db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
}

ADD_APPS = (
    'gitmanager',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

LOGGING['loggers'].update({
    '': {
        'level': 'INFO',
        'handlers': ['console'],
        'propagate': True,
    },
    #'django.db.backends': {
    #    'level': 'DEBUG',
    #},
})

# kate: space-indent on; indent-width 4;
# vim: set expandtab ts=4 sw=4:
