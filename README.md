# django-products-example
Simple example of Django CRUD application implemented with Class Based Views and Twitter Bootstrap. 
What can you find here:
* CRUD-operations for managing `Product` model implemented with [Class Based Views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/).
* UI developed with [Bootstrap 4.1.1](https://getbootstrap.com/).
* Model validation with [ModelForm](https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/) and [Model.clean](https://docs.djangoproject.com/en/2.0/ref/models/instances/#validating-objects) method.
* Product list filtration implemented with [django-filter](http://django-filter.readthedocs.io/en/latest/).
* Example of custom form widget `PriceWidget`.
* User registration and authentication example with [Django auth views](https://docs.djangoproject.com/en/2.0/topics/auth/default/#module-django.contrib.auth.views).
* Access limiting for CRUD-operations based on user permissions with [PermissionRequiredMixin](https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-permissionrequiredmixin-mixin).
* [Custom template tags and filters](https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/).
* Reusable template components (`templates/pagination.html`, `templates/form_inputs.html`, `templates/form_submit.html`) and so on.

# Installation

1. Install [Python 3.6](https://www.python.org/downloads/release/python-366/).
2. Check whether you have pip installed with your Python:
```bash
pip help
```

If pip is not installed, then you can read [here](https://pip.pypa.io/en/stable/installing/) how to download and install it.   
**Pip** will help you to install required packages into this project by simply typing one command to your terminal.

3. Install virtualenv. VirtualEnv is a powerful tool to create isolated Python environments.
```bash
pip install virtualenv
```

4. Create a virtual environment in your project directory.
```bash
cd <project_directory>
virtualenv -p python3.6 .\venv
```

5. Start a virtual environment:

**Windows**
```bash
.\venv\Scripts\activate
```

**Linux\OSX**
```bash
source .\venv\bin\activate
```

6. Install project requirements with **pip**:
```bash
pip install -r requirements.txt
```

7. Create test database by running Django-migrations. This command will create a simple SQLite-database named *db.sqlite3* in project directory:
```
python manage.py migrate
```

8. *[Optional]* Load fixtures for initial data.
```bash
python manage.py loaddata data.json
```

# Run

To run this project now first of all you need to start your virtual environment (Installation - Step 5). 
After that you probably want at least one administrator of this system to manage products data. You can create superuser for this system by running next command:
```bash
python manage.py createsuperuser
```

Now you can run your development server by typing the next command, to stop the server just press **Ctrl + C**:
```
python manage.py runserver
```
