# DJ Simple auth TODO

python 3.8.13

## Entorno virtual

### Conda

```
conda create -n djTodo python=3.8
conda activate djTodo
```

### virtualenv

```
virtualenv venv
source venv/bin/activate
```

Windows: https://sectorgeek.com/instalar-python-pip-y-virtualenv-en-windows-10/

## Instalar paquetes

```
pip install -r ./serve/requirements.txt
```

## inicializar Base de Datos

```
python manage.py migrate
```

## crear un superusuario

```
python manage.py createsuperuser
```

## Correr el Proyecto

```
python manage.py runserver
```

## urls

* Proyecto corre en http://localhost:8000
* página de administración es 