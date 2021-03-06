import os
import sys

from django.conf import settings

# get DEBUG from environment, default to on
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
# default to random num if not set
SECRET_KEY = os.environ.get('SECRET_KEY', 'a+$s!_$uu&nnm2afi^gdgs!$$2o8=zgkn4r%w^lod!5)-f%sf9')
# default to localhost if none set
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Need to set up these settings before making any additional imports from Django
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

application = get_wsgi_application()

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)

# if called with interpreter, run with command line options
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
