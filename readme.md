# introduccion a django

Usa MVT (modelo vista template) no es como mvc la vista procesa y el template es el html o lo que ve el usuario


```shell
django-admin startproject [nombre]
cd [nombre]


pip install virtualenv
virtual env [nombre]


mkdir apps //para las aplicaciones
cd apps
touch __init__.py
```

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

## Tips

en vs code vincula `django-html: html` en configuracion de emmet

vscode tiene plugin para django




## Modelos

por defecto usa sqlite3, sin embargo soporta mysql, oracle, postgres y en la version 3 mariadb de forma nativa si quieres usar algo mas usa un plugin externo

se tiene gestion de permisos por defecto y al migrar tendremos mas tablas a cada modelo se le generar permisos de crud

dentro de cada aplicacion se generan sus migraciones

1. Crear el modelo de la tabla dentro models.py
2. En la raiz correr `python manage.py makemigrations`
3. creara el archivo que corre las migraciones detro de el folder migrations de cada aplicacion 0001_initial.py
4. ejecutar (migrar) los archivos creados con `python manage.py migrate`



## Admin

para servir la app debemos correr las migraciones iniciales y despues :

```shell
python manage.py runserver
```

Tenemos por defecto la ruta admin con cruds, sin embargo no podemos acceder sin un usuario que no se crea por defecto.
para crearlo vamos a la terminal y ecribimos `python manage.py createsuperuser`.

Dentro de admin.py de cada componente debemos registrar los modelos para tener un crud basico

admin.py

```python
admin.site.register([NombreClaseModelo])
# ej:
admin.site.register(Persona)
```

dentro de views.py podemos definir vistas tipo funcion que regresen de render

```python
from .models import model

def inicio(request):
    return render(request, 'index.html')
```

la registrtamos dentro de urls.py

```python
from apps.principal.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path(route='', view=inicio, name='index')
]
```

en el archivo de settings se debe configurar el path de los templates y django lo buscara en todo el proyecto aqui los archivos seran encontrados.

settings.py
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
    }
]
```