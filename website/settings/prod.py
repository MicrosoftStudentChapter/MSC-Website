from website.settings.common import *  # noqa
import os
import dj_database_url


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = []

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES["default"].update(db_from_env)  # noqa
