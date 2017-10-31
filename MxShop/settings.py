"""
Django settings for MxShop project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import datetime
import os
import sys
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4-h89d3$jvte35m^_1)j^+4=uxk0356!uct54a+t_!v9cc%m1q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

HOST = '39.106.14.35'
PORT = '8000'
ALLOWED_HOSTS = ["*", ]

# 自定义user表结构
AUTH_USER_MODEL = 'users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',
    'users.apps.UsersConfig',
    'goods.apps.GoodsConfig',
    'trade.apps.TradeConfig',
    'user_operation.apps.UserOperationConfig',
    'crispy_forms',
    'xadmin',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'rest_framework.authtoken',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 要放在CommonMiddleware之前
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 应许跨域
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'MxShop.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mxshop",
        'USER': 'root',
        'HOST': HOST,
        'PASSWORD': "123456",
        'PORT': '3306',
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB'}
        # 'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 设置时区
LANGUAGE_CODE = 'zh-hans'  # 中文支持，django1.8以后支持；1.8以前是zh-cn

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False   # 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！

# 自定义认证
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBBackend',
    'social_core.backends.weixin.WeixinOAuth2',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = "/media/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 所有关于rest_framework的配置
# REST_FRAMEWORK = {
#     'PAGE_SIZE': 100,
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',  # 全局Token不能解决公共数据的问题
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 全局Token不能解决公共数据的问题
    ),
    # IP限速
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '60/minute',
        'user': '60/minute'
    }
}

# 认证设置0 .
JWT_AUTH = {
    " JWT_EXPIRATION_DELTA": datetime.timedelta(hours=1, minutes=100, seconds=0),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',  # 对应里面的前缀 "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1N
}

# 云片网Key
API_KEY = "672da4b47c4d7b77571b3bec872c1d88"

# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"


# QQ
SOCIAL_AUTH_QQ_KEY = 'foobar'
SOCIAL_AUTH_QQ_SECRET = 'bazqux'

# 微博
SOCIAL_AUTH_WEIBO_KEY = "3084778121"
SOCIAL_AUTH_WEIBO_SECRET = "6ddb49464400f59872169e2c917ddc33"

# 微信
SOCIAL_AUTH_WEIXIN_KEY = 'foobar'
SOCIAL_AUTH_WEIXIN_SECRET = 'bazqux'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'

# 缓存时长设置
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 100
}
# 缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 支付宝相关配置
ALIPAY_ID = "2016080900196283"
private_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/private_2048.txt')
ali_pub_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/alipay_key_2048.txt')
app_notify_url = "http://{host}:{port}/alipay/return/".format(host=HOST, port=PORT)
return_url = "http://{host}:{port}/index/#/app/home/member/order".format(host=HOST, port=PORT)
