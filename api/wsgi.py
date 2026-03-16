"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``app``.

For information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = get_wsgi_application()

# Startup hooks: migrate e (em Vercel) garantir collectstatic para manifest/estáticos.
try:
    call_command('migrate', interactive=False, verbosity=0)
    if os.environ.get('VERCEL'):
        call_command('collectstatic', interactive=False, verbosity=0)
except Exception as e:
    print(f"Erro na migração/collectstatic: {e}")
