"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``app``.

For information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = get_wsgi_application()

# --- ADICIONE ISTO AQUI EM BAIXO ---
from django.core.management import call_command
try:
    # Isto cria as tabelas na pasta /tmp do Vercel assim que o site liga
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Erro na migração: {e}")
