python -m venv venv
source venv/bin/activate  #use `env\Scripts\activate`

pip install django
pip install djangorestframework

django-admin startproject livraria .

django-admin startapp livraria_progama

python manage.py migrate
