from website.settings.base import *  # noqa
import os
import dj_database_url


SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5Asj6yjpkag"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = []


# Postgres Database configuration

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)  # noqa
