from website.settings.base import *  # noqa
import os


SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5Asj6yjpkag"
)

DEBUG = os.environ.get("DJANGO_DEBUG", "") != "False"

ALLOWED_HOSTS = []
