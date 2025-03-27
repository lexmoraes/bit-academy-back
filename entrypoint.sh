#!/bin/sh

# Aguarda até que o banco de dados esteja pronto e não dar problema na hora de acessar.
until python manage.py check --database default; do
  echo "Aguardando o banco de dados..."
  sleep 2
done

# Aplica migrações para atualizar o banco.
echo "Aplicando migrações..."
python manage.py migrate

# Coleta arquivos estáticos.
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Inicia o servidor Gunicorn em Produção ou Django em outros ambientes.
if [ "$DJANGO_ENV" = "production" ]; then
  echo "Iniciando Gunicorn..."
  exec gunicorn --bind 0.0.0.0:8000 bit_academy.wsgi:application
else
  echo "Iniciando runserver..."
  exec python manage.py runserver 0.0.0.0:8000
fi