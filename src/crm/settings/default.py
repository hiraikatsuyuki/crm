import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "=ctceo4()$%8nj$a4g!ag6*6z-o8lkneoih$xp(bxv0rg=pb1&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "adminlte3",
    "base",
    "nayose",
    "shokuinroku",
    "researcher",
    "application",
    "seminar",
    "promotion",
    "kaken",
    "consignment",
    "matching",
    "reviewer",
    "accounts",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "import_export",
    # "bootstrap4",
    "bootstrap_datepicker_plus",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crm.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR),
            "templates",
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "crm.wsgi.application"


# Database

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "crm",
#         "USER": "root",
#         "PASSWORD": "3wf5qnPbnA7q",
#         "HOST": "mysql",
#         "PORT": "3306",
#         "OPTIONS": {"charset": "utf8mb4"},
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'crm.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization

LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/crm/static/"
STATIC_ROOT = "/static"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


# crispy-forms
# CRISPY_TEMPLATE_PACK = "bootstrap4"

# allauth
# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     "allauth.account.auth_backends.AuthenticationBackend",
# )
# ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_VERIFICATION = "none"
# ACCOUNT_EMAIL_REQUIRED = True

# SITE_ID = 1

# LOGIN_REDIRECT_URL = "base:front"
# ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/"


#
# Local Settings
#

# Django_debug_toolbar
# def show_toolbar(request):
#     return True


# INSTALLED_APPS += ("debug_toolbar",)
# MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
# DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": show_toolbar}