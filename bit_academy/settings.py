import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

ENVIROMENT = os.getenv("DJANGO_ENV", "development")
if ENVIROMENT != "production":
    ENV_FILE = ".env.development"
    env_path = BASE_DIR / ENV_FILE
    if env_path.exists():
        load_dotenv(env_path)
    else:
        raise FileNotFoundError(f"Arquivo de ambiente '{ENV_FILE}' não encontrado.")

SECRET_KEY = os.getenv("SECRET_KEY", "123456")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Other apps
    "rest_framework",
    "drf_yasg",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.linkedin',
    # Our apss
    "bit_main"

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
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "bit_academy.urls"

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

WSGI_APPLICATION = "bit_academy.wsgi.application"

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

DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Provider specific settings
'''SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}'''

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
