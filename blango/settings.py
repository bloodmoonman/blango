"""
Django settings for blango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from configurations import Configuration
from configurations import values
import dj_database_url



class Dev(Configuration): #in development

  # Build paths inside the project like this: BASE_DIR / 'subdir'.
  BASE_DIR = Path(__file__).resolve().parent.parent

  EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
  ACCOUNT_ACTIVATION_DAYS = 7 #the time for users to activate their acc

  #REGISTRATION_OPEN = False we can close the registration for users, so they can't create an account

  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True

  ALLOWED_HOSTS = values.ListValue(["localhost", "0.0.0.0", ".codio.io"])
  X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
  CSRF_COOKIE_SAMESITE = None
  CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SAMESITE = 'None'
  SESSION_COOKIE_SAMESITE = 'None'
  CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
  CRISPY_TEMPLATE_PACK = "bootstrap5"

  REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "blog.api.throttling.AnonSustainedThrottle",
        "blog.api.throttling.AnonBurstThrottle",
        "blog.api.throttling.UserSustainedThrottle",
        "blog.api.throttling.UserBurstThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon_sustained": "500/day",
        "anon_burst": "10/minute",
        "user_sustained": "5000/day",
        "user_burst": "100/minute",
    },
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,

    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.OrderingFilter"
    ],
  }

  AUTH_USER_MODEL = "blango_auth.User"
  # Application definition

  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      "blango_auth",
      'blog',
      'crispy_forms',
      'crispy_bootstrap5',
      "debug_toolbar",
      "rest_framework",
      "rest_framework.authtoken",
      "django_filters",
      
  ]
  
  PASSWORD_HASHERS = [
      'django.contrib.auth.hashers.Argon2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
      'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
  ]

  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      #'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      #'django.middleware.clickjacking.XFrameOptionsMiddleware',
      "debug_toolbar.middleware.DebugToolbarMiddleware",
  ]
  INTERNAL_IPS = ["192.168.11.179"]

  ROOT_URLCONF = 'blango.urls'

  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]

  WSGI_APPLICATION = 'blango.wsgi.application'


  # Database
  # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

  DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")

      #  DATABASES = {                        CHANGED THIS TO LINE 95, BE AWARE.
            #'default': {
            #   'ENGINE': 'django.db.backends.sqlite3',
              #  'NAME': BASE_DIR / 'db.sqlite3',
            #}
        #}
  LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
  }




  # Password validation
  # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

  AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]


  # Internationalization
  # https://docs.djangoproject.com/en/3.2/topics/i18n/

  LANGUAGE_CODE = 'en-us'

  TIME_ZONE = values.Value("UTC")

  USE_I18N = True

  USE_L10N = True

  USE_TZ = True


  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/

  STATIC_URL = '/static/'

  # Default primary key field type
  # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

  DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





class Prod(Dev): #in production
  DEBUG = False # definitely want DEBUG to be False in production for security reasons
  SECRET_KEY = values.SecretValue()
  #DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3") # /// indicates the empty hostname


  

