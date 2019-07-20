"""
Django settings for MemoryMapProject project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*p3+zw1n-&5@*5&glk^lv4^l4z*5m%r#ms5+-y(m++t1-)wh8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition


# # 사용자 지정 유저 모델
# AUTH_USER_MODEL = 'accounts.User'

# allauth 세팅
SITE_ID = 1
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = 'accounts/login/'

# allauth가 django의 인증체계를 사용할 수 있도록 설정
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend", # 기본인증
    "allauth.account.auth_backends.AuthenticationBackend", # 추가적인 인증
)

CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',     # form에 bootstrap 적용

    'blog.apps.BlogConfig',
    'taggit',           # 태그관련 기능 https://django-taggit.readthedocs.io/en/latest/getting_started.html
    'django_countries', # CountryField 사용 https://pypi.org/project/django-countries/
]

INSTALLED_APPS += [
    'django.contrib.sites',

    # 공식 레퍼런스 https://django-allauth.readthedocs.io/en/latest/views.html
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 원하는 provider를 enable https://github.com/YeongBaeeee/practice/wiki/26-OAuth-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EA%B3%BC-%EB%8F%99%EC%8B%9C%EC%97%90-%EB%A1%9C%EA%B7%B8%EC%9D%B8
    # 'allauth.socialaccount.providers.facebook', 
    # 'allauth.socialaccount.providers.kakao', 
    # 'allauth.socialaccount.providers.naver', 
    'allauth.socialaccount.providers.github', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MemoryMapProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # for allauth
                'django.template.context_processors.request', 
            ],
        },
    },
]

WSGI_APPLICATION = 'MemoryMapProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# 1.python manage.py collectstatic
# 2.Yes
# 3.All static files are collected to STATIC_ROOT
import os

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
