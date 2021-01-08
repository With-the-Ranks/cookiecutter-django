{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/With-the-Ranks/cookiecutter-django/
     :alt: Built with Cookiecutter Django (WTR fork)
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Setup
--------
1. Clone the repo locally.

::

$ git clone https://github.com/With-the-Ranks/{{cookiecutter.project_slug}}.git

2. Create pipenv environment

::

$ cd {{cookiecutter.project_slug}}
$ pipenv --python 3.8.5
$ pipenv install

3. Install frontend packages.

::

$ npm install

4. Compile assets

::

$ npm run build

5. Create database

::

$ createdb {{cookiecutter.project_slug}}

6. Run migrations

::

$ pipenv run ./manage.py migrate

7. Run server

::

$ npm run dev

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ pipenv run ./manage.py createsuperuser


Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html
