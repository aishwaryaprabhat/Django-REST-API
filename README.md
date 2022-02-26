# Django-REST-API
A REST API built using the following technologies:
- Django
- Django REST framework
- Travis CI
- Postgres

## Useful commands
-  Starting project
```
docker-compose run app sh -c "django-admin.py startproject app ."
```
-  Running unit tests
```
docker-compose run app sh -c "python manage.py test && flake8"
```