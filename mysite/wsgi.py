import os, sys
sys.path.insert(0, '/var/www/u1585313/data/www/greenavicash.ru/mysite')
sys.path.insert(1, '/var/www/u1585313/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()