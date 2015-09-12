#!/usr/bin/env python

import sys
import django
from os.path import dirname, abspath

from django.conf import settings



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
        'semanticuiform',
    ],
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    SITE_ID=1,
    DEBUG=False,
    ROOT_URLCONF='',
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
    failures = test_runner.run_tests(['semanticuiform'], test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
