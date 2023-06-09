"""
Настройки Django для проекта empserv.

Сгенерировано «django-admin startproject» с использованием Django 4.0.7.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.0/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os

from pathlib import Path

"""  Comment  """


# ОСНОВНАЯ ДИРЕКТОРИЯ Создайте пути внутри проекта, как это: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого старта разработки — не подходят для продакшена
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# ВНИМАНИЕ ПО БЕЗОПАСНОСТИ: держите секретный ключ, используемый в производстве, в секрете!
SECRET_KEY = 'django-insecure-ood$#r$y8m$(_h7quz(#tyl43sm89oj_^_#s%v1cp3wss1m@-6'

# ПРЕДУПРЕЖДЕНИЕ О БЕЗОПАСНОСТИ: не запускайте программу с включенной отладкой! Поставить False когда сайт на хостинге будет уже
DEBUG = True

ALLOWED_HOSTS = []


# Определение приложения

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'events.apps.EventsConfig',
    #'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

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

ROOT_URLCONF = 'empserv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':['templates'],
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

WSGI_APPLICATION = 'empserv.wsgi.application'


# База данных
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {

       # 'ENGINE': 'django.db.backends.sqlite3',   # Настройки БД по умолчанию
      #  'NAME': 'os.path.join(BASE_DIR, 'db.sqlite'),  # Настройки БД по умолчанию


        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'empservdb',
        'USER': 'postgres',
        'PASSWORD': 'cen78ter19',
       # 'HOST': 'http://127.0.0.1:8000', # Расположение БД, указываем адрес нашего сервера
        'HOST': 'localhost', 
        'PORT': '5432', # Порт БД
}
}

# Проверка пароля
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Интернационализация
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, Изображений)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATICFILES_DIRS = [  # Папки со статичными файлами
    os.path.join(BASE_DIR, 'empserv/static/')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Основная папка для хранения файлов
STATIC_URL = 'static/'


# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Основная папка для хранения файлов

MEDIA_URL = '/empserv_media/' # Здесь указываем какое имя у папки будет отображаться
# в адресной строке браузера при построении url-адреса. Имя MEDIA_ROOT 
# не должно быть таким же как в MEDIA_URL
#
#