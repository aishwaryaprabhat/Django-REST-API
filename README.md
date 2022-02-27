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
- Creating a new app 
```
docker-compose run app sh -c "python manage.py startapp core"
```
- Make migrations
```
docker-compose run app sh -c "python manage.py makemigrations core"
```
- Create super user
```
docker-compose run app sh -c "python manage.py createsuperuser"
```

## General Flow (TDD)
- Add test for creating object
- Add model for object
- Register model in admin
- Add test for listing objects
- Add feature for listing objects