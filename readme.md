# introduccion a django

usa MVT (modelo vista template) no es como mvc la vista procesa y el template es el html o lo que ve el usuario


django-admin startproject [nombre]
cd [nombre]


pip install virtualenv
virtual env [nombre]


mkdir apps //para las aplicaciones
cd apps
touch __init__.py


dentro de apps u otra meteremos las aplicaciones
las aplicaciones son modulos

```shell
django-admin startapp [nombre]
```

debemos registrar dentro de settings.py por ejemplo

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.principal',
]
```


## Modelos

por defecto usa sqlite3, sin embargo soporta mysql, oracle, postgres y en la version 3 mariadb de forma nativa si quieres usar algo mas usa un plugin externo

se tiene gestion de permisos por defecto y al migrar tendremos mas tablas a cada modelo se le generar permisos de crud

dentro de cada aplicacion se generan sus migraciones

1. Crear el modelo de la tabla dentro models.py
2. En la raiz correr `python manage.py makemigrations`
3. creara el archivo que corre las migraciones detro de el folder migrations de cada aplicacion 0001_initial.py
4. ejecutar (migrar) los archivos creados con `python manage.py migrate`
