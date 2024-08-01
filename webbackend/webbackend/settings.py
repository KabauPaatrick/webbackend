import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the media directory where uploaded media files will be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Define the base URL for serving media files
MEDIA_URL = '/media/'

# Define the base URL for serving static files
STATIC_URL = '/static/'

# Define additional directories from which to serve static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Define the directory where collected static files should be stored
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=@os3v93jvz35l8__#9lvbfevb%mz5c0%&lhco@2!&saqe&hem"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    "corsheaders",
    'authemail',
    
    'accounts',
    'achievemets',
    'customer',
    'entity',
    'tickets',
    'solutions',
    'socials',
    'comments',
    'Benefit',
    'Homeview',
    'HeroPage',
    'testimonials',
    'license',
    'users',
    # 'logo',
    'product',
     'cloudinary',
    'cloudinary_storage',
    'category',
    'brands',
    'colors',
    'Enquiry',
    'payments',
    'FileUpload'

]
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dkekd92kz',
    'API_KEY': '187641184772337',
    'API_SECRET': '8Hwz-YRED2DXRsspD_wzNDO67OI',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_URL = 'cloudinary://187641184772337:8Hwz-YRED2DXRsspD_wzNDO67OI@dkekd92kz'


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "webbackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "webbackend.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'disiweb',
        'USER': 'root',
        'PASSWORD': 'Pato@254',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'OPTIONS': {
        #     'unix_socket': '/var/run/mysqld/mysqld.sock',  
        # },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
     'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ),
}

EMAIL_BACKEND = 'django.core.mail.backends.async.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'kabaupaatrick@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'pwci uumf rbhj vjdg'  # email pass 
DEBUG_EMAIL = True


AUTH_USER_MODEL = 'users.User'