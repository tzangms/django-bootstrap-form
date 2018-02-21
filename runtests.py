#!/usr/bin/env python

import sys
import django
from os.path import dirname, abspath

from django.conf import settings

middleware = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )


if django.VERSION < (1, 10):
    middleware_arg = {
        'MIDDLEWARE_CLASSES': middleware,
    }
else:
    middleware_arg = {
        'MIDDLEWARE': middleware,
    }

settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'bootstrapform',
    ],
    SITE_ID=1,
    DEBUG=False,
    ROOT_URLCONF='',
    TEMPLATES = [  # For >= Django 1.10
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.contrib.auth.context_processors.auth',
                ],
            },
        },
    ],
    **middleware_arg
)


def runtests(**test_args):
    from django.test.utils import get_runner

    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)

    try:
        django.setup()
    except:
        pass

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['bootstrapform'], test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
