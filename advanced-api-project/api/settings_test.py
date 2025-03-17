""" 
This settings configuration is intende to be used for
testing, isolating the development and production databases
to avoid unintended errors/modifications
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite',
        'NAME': 'bookapi_db.sqlite',
    }
},