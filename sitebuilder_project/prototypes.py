import sys

from django.conf import settings



settings.configure(
    DEBUG=True,
    SECRET_KEY='aldskfja;lsdkfj;ladskfj;ald',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        # application for creating placeholder text in our apps
        'django.contrib.webdesign', 
        'sitebuilder',
    ),
    STATIC_URL='/static/',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
