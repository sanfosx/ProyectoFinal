# Sitio Web desarrollado por el Grupo 9 de la Comision 4 del Curso de Programacion Web del Informatorio 2021

_Primer proyecto proyecto del modulo de desarollo web_
_Usando template base: https://getbootstrap.com/docs/5.1/examples/cover/


_Proyecto Web Aniversario del Chaco del Modulo de Desarollo web_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

```
git clone https://github.com/sanfosx/ProyectoFinal
```

### Pre-requisitos 📋

_Instalar las dependendencias del proyecto (ir a la carpeta de requirements)_

```
pip install -r base.txt
```

_Crear settings local.py_

from .base import *
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'NombreBaseDeDatos',
        'USER': 'UsuarioBaseDeDatos',
        'PASSWORD': 'ContraseñaBaseDeDatos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
_Importar los datos en la Base de Datos_

_Para probar el proyecto se deben cargar las preguntas, esto se puede realizar cargando el archivo **bdgrupo4.json** por CMD (que incluye la Base de Datos completa con preguntas y usuarios de prueba) o bien el archivo bdgrupo4.csv (que contiene sólo las preguntas) desde el gestor de Base de Datos. Ambos archivos se encuentran en la carpeta **_docs_** del Proyecto._

## Construido con 🛠️

* [Django]Framework web
* [PostgreSQL]Base de datos


## Autores ✒️

* **Santiago Foschiatti** - *Student* - [sanfosx]
* **Ricardo Lindow** - *Student* - [richardlindow]
* **Pablo Ramirez** - *Student* - [pabloandramirez]
* **Hugo Rostan** - *Student* - [HugoR19]
* **Cristian Oviedo** - *Student* - [Cristian934]
* **Lucas Ibañez** - *Developer* - [lucasibaniez]

### Video Demostrativo y Manual del Usuario:

_Se puede acceder desde:_ https://drive.google.com/drive/folders/10l6z6KXNO-wBVqrLEx8HE8qd4o7XnA0S

_Visualizar el video:_ https://youtu.be/d6Vavzoiz_U

---
