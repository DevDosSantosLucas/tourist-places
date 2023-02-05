para funcionar corretamente no curso:
pip install django==2.0.1
https://www.djangoproject.com/
https://www.django-rest-framework.org/ 

Passao-a-passo CDM:
python -m venv venv
C:\www\django\api-rest>cd venv\Scripts\          
C:\www\django\api-rest\venv\Scripts>activate
(venv) C:\www\django\api-rest\venv\Scripts>cd ../../


(venv) C:\www\django\api-rest>pip install django==2.0.1
(venv) C:\www\django\api-rest>django-admin startproject tourist_places .  

(venv) C:\www\django\api-rest>pip install djangorestframework
colocar em setting:
INSTALLED_APPS = [
    ...
    'rest_framework',
]


(venv) C:\www\django\api-rest>python manage.py migrate
(venv) C:\www\django\api-rest>python manage.py createsuperuser
user: admin - password: admin123
(venv) C:\www\django\api-rest>python manage.py runserver 

(venv) C:\www\django\api-rest>python manage.py startapp core  

criar os models : ../core/models
criar no admin ../core/admin

(venv) C:\www\django\api-rest>python manage.py makemigrations
(venv) C:\www\django\api-rest>python manage.py migrate


IMAGENS:
(venv) C:\www\django\api-rest>pip install Pillow

filtragem DJANGO FILTER
(venv) C:\www\django\api-rest>pip install django-filter

from rest_framework import filters
  lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '@': 'search',
        '$': 'iregex',
    }
