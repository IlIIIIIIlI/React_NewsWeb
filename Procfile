web: gunicorn sputnik_news.wsgi
release: python manage.py makemigrations news
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
