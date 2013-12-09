"""Settings for Development Server"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dinner',
        'USER': 'django',
        'PASSWORD': 'djangoadmin',
        'HOST': 'dinner.micfan.com',
        'PORT': '5432'
    }
}



# WSGI_APPLICATION = 'src.wsgi.dev.application'
