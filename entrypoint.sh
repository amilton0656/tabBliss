#!/usr/bin/env bash
set -e

echo "Aguardando Postgres em ${DB_HOST}:${DB_PORT}..."
python - <<'PY'
import os, socket, time
h=os.getenv("DB_HOST","127.0.0.1"); p=int(os.getenv("DB_PORT","5432"))
for _ in range(60):
    try:
        with socket.create_connection((h,p), timeout=2): print("Postgres OK"); break
    except OSError: time.sleep(1)
else:
    raise SystemExit("Timeout aguardando Postgres")
PY

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn bliss_project.wsgi:application \
  --bind 0.0.0.0:8000 --workers 3 --timeout 120
