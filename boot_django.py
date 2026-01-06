"""
This file sets up and configures Django. It's used by scripts that need to
execute as if running in a Django server.
"""

import os

import django
from django.conf import settings


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "i54m_apiuser"))


def boot_django():

    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        AUTH_USER_MODEL = 'i54m_apiuser.ApiUser',
        DATABASES={
            "default":{
                "ENGINE":"django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "i54m_apiuser",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
        TEST_RUNNER = "xmlrunner.extra.djangotestrunner.XMLTestRunner",
        TEST_OUTPUT_DIR=os.path.join(BASE_DIR, "test-results"),
    )

    django.setup()