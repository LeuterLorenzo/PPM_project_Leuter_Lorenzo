import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PPM_progect_Leuter_Lorenzo.settings')

application = get_wsgi_application()