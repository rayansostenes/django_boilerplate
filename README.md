# Django Boilerplate
A standard convention for Django app layouts

## Environment Variables
- **DJANGO_SETTINGS_MODULE**
- **DATABASE_URL**

## Directory Structure
```
├── apps
│   └── __init__.py
├── lib
│   └── __init__.py
├── settings
│   ├── __init__.py
│   ├── dev.py
│   ├── local.py
│   ├── settings.py
│   └── staging.py
├── templates
│   └── base.html
├── manage.py
├── README.md
├── media
├── urls.py
├── wsgi.py
├── Pipfile
└── Pipfile.lock
```

### lib
Python packages and modules that aren't true Django 'apps' - i.e. they don't have their own models, views or forms. These are just regular Python classes and methods, and they don't go in the INSTALLED_APPS list of your project's settings file.

### settings
Settings for django, separated by environment 

### templates
Project-wide templates (i.e. those not belonging to any specific app in the apps/ folder).

### manage.py
The standard Django manage.py.

### urls.py
Barebones url_patterns.

