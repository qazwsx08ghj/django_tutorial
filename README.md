# Django Turorial

This is a tutorial for Django.

## Installation

### 1.Install Python

### 2.Install MariaDB

### 3.To install Django, run the following command:

    $ pip install django

### Creating a project

    $ django-admin startproject mysite

### Creating an app

    $ py manage.py startapp website

### Running the server

    $ py manage.py runserver

### change settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'your/config/file/path', #example: 'config/my.cnf'
        },
    }
}
```

### Migrating the database
    $ py manage.py migrate

### Creating a superuser

    $ py manage.py createsuperuser
