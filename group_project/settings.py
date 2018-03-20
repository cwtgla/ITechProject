import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))

# new variable for the login - redirecting the uses to registration
LOGIN_URL = '/FriendsFinder/login/'

LOGIN_REDIRECT_URL = '/FriendsFinder'

REGISTRATION_OPEN = True

ACCOUNT_ACTIVATION_DAYS = 7

REGISTRATION_AUTO_LOGIN = True


# a new variable called TEMPLATE_DIR that will reference
# your new templates directory.
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# new variable pointing to our static directory
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# media files will be uploaded to Django project’s root
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*p)*6@q(81g(y+mry8iizxy+x934b^$i)(l4rjvd@pyjuh(m16'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'FriendsFinder',
	'social_django',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
	
)
SITE_ID = 1

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is were emails and domains whitelists are applied (if
    # defined).
    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social.pipeline.user.create_user',

#	'app2.utils.print_email',



    # Create the record that associated the social account with this user.
    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social.pipeline.user.user_details',
)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware', 
]

ROOT_URLCONF = 'group_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.media',
				'social.apps.django_app.context_processors.backends',
				'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '909110158459-kb1ubolo266u79l20c7pjkj61q9k1p97',
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'lYKj53TuMsrOXZ3MF5FI3gb6',


AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social_core.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
   'social_core.backends.open_id.OpenIdAuth',
)

WSGI_APPLICATION = 'group_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [STATIC_DIR, ]

SOCIAL_AUTH_FACEBOOK_KEY = '116114165838276'
SOCIAL_AUTH_FACEBOOK_SECRET = '9da9b67d2fabbf8fb9aec3dcdd9bfe4c'

SOCIAL_AUTH_TWITTER_KEY = '5oDQfyQ5FZjAi4di5XSwiICLt'
SOCIAL_AUTH_TWITTER_SECRET = 'zgioiW12EO1O2Q3BzhDTl0GPO7ooyu6pUsd8JUd9EDtKqoNt5R'

