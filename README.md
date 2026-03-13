
# Wall of Kind Messages

A simple Django project where people can share positive messages.

## O que foi ajustado
- Configuração de estáticos apontando para `kindwall/static` (onde estão os CSS).
- Build do Vercel agora roda `python manage.py collectstatic --noinput` e serve arquivos de `/staticfiles`.

## Como rodar localmente
1) Criar ambiente: `python -m venv .venv` e ativar (`.\.venv\Scripts\Activate` no PowerShell).  
2) Instalar deps: `pip install -r requirements.txt`.  
3) Migrações: `python manage.py migrate`.  
4) (Opcional) Coletar estáticos: `python manage.py collectstatic --noinput`.  
5) Subir: `python manage.py runserver` e acessar `http://127.0.0.1:8000/`.

## Deploy no Vercel
- O runtime é Python 3.12 (ver `runtime.txt`).
- O build executa `python manage.py collectstatic --noinput` para gerar `staticfiles/`.
- Rotas do Vercel servem `/static/` a partir de `/staticfiles/` e o restante vai para `api/wsgi.py` (WhiteNoise).
- Banco SQLite fica em `/tmp/db.sqlite3` quando em produção na Vercel.

## Tech
- Python 3.13
- Django 5.x
- SQLite (default database)
