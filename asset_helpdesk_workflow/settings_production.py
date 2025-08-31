import os
from decouple import config
from .settings import *

DEBUG = False


ALLOWED_HOSTS = ['your-app-name.onrender.com', 'localhost', '127.0.0.1']


import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default'sqlite://db.sqlite3),
        conn_max_age=600
    )
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


CSRF_TRUSTED_ORIGINS = [
    'https://your-app-name.onrender.com',
    'http://localhost:8000',
    'http://127.0.0.1:8000'
]


SECRET_KEY = config('SECRET_KEY', default=SECRET_KEY)