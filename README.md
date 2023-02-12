  <img src="https://img.shields.io/badge/WEB-OK-green">     <img src="https://img.shields.io/badge/SERVER-OK-green">    <img src="https://img.shields.io/badge/API-OK-green"> <img src="https://img.shields.io/badge/LICENÇA-MIT-green"> 
 <h1>TOURIST PLACES API </h1>
 <a href="https://www.djangoproject.com/" target ="_blank">
  <img src= "https://img.shields.io/badge/DJANGO-092e20?style=for-the-badge&logo=django&logoColor=white" />
</a>
 <a href="https://www.django-rest-framework.org/" target ="_blank">
  <img src= "https://img.shields.io/badge/Django_Rest_Framework-red?style=for-the-badge&logo=Django&logoColor=white" />
</a>
 <a href="https://www.python.org/" target ="_blank">
  <img src= "https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=Python&logoColor=white" />
</a>

 
![image](https://user-images.githubusercontent.com/37936745/218315752-ee8db175-5bcf-49f6-a9f7-f5859dbf3850.png)


<h2>pip install:</h2>

    pip install django==2.0.1
    pip install djangorestframework
    pip install Pillow
    pip install django-filter

    
<p>Esse conteúdo foi realizado com instrução do curso

[Apis Restful com Django Rest Framework](https://www.udemy.com/course/apis-restful-com-django-rest-framework/) </p>

<h2>Anotações: para funcionar corretamente no curso: </h2>

    pip install django==2.0.1
    
    Passao-a-passo cmd:
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

