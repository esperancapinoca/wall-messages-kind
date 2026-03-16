
# Wall of Kind Messages

Projeto Django simples para compartilhar mensagens positivas.

## Mudanças recentes
- Estáticos: `STATICFILES_DIRS` aponta para `kindwall/static`; backend usa `whitenoise.storage.CompressedStaticFilesStorage` + `WHITENOISE_USE_FINDERS=True` para evitar 404/500 quando o manifest não existe em ambiente serverless.
- `api/wsgi.py` executa `migrate` e, se `VERCEL` estiver setado, também `collectstatic` no startup.
- `vercel.json` roda `python manage.py collectstatic --noinput`; todo tráfego passa por `api/wsgi.py` (WhiteNoise serve `/static/...`).
- Testes em `kindwall/tests.py` cobrem render da página, fluxo de criar/curtir mensagem e verificação de estáticos.

## Como rodar localmente
1) Criar e ativar venv: `python -m venv .venv` e `.\.venv\Scripts\Activate` (PowerShell).  
2) Instalar dependências: `pip install -r requirements.txt`.  
3) Migrações: `python manage.py migrate`.  
4) (Opcional) Coletar estáticos: `python manage.py collectstatic --noinput` (gera `staticfiles/`).  
5) Subir: `python manage.py runserver` e acessar `http://127.0.0.1:8000/`.  

## Testes
- Rodar: `python manage.py test`.  
- Abrange:  
  - Página `wall` responde 200 e inclui links dos CSS.  
  - Criar mensagem e like incrementam contadores.  
  - Estáticos são encontrados pelos finders e servidos via storage (URL hashada quando manifest existe).  

## Deploy no Vercel
- Runtime: Python 3.12 (`runtime.txt`).  
- Build: `python manage.py collectstatic --noinput`.  
- Roteamento: `/(.*)` → `api/wsgi.py`; WhiteNoise serve `/static/...`.  
- Banco: SQLite em `/tmp/db.sqlite3` quando `VERCEL` está presente (filesystem efêmero).  

## Troubleshooting (produção)
- 500/404 de estáticos: mitigado com `CompressedStaticFilesStorage` + `WHITENOISE_USE_FINDERS=True`; confirme nos logs se `collectstatic` rodou.  
- CSS não atualiza: rode `collectstatic` e faça novo deploy (ou use `collectstatic --clear` antes).  
- Startup falha: verifique mensagens do `api/wsgi.py` sobre `migrate`/`collectstatic` nos logs do Vercel.  

## Tech
- Python 3.12
- Django 6.x
- SQLite (default database)
