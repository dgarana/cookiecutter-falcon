{{ cookiecutter.project_name }}
==============================

{{ cookiecutter.project_description }}

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

{% if cookiecutter.open_source_license != "Not open source" %}
LICENSE: {{ cookiecutter.open_source_license }}
{% endif %}

Deployment
----------
Local
^^^^^

To deploy the app locally (for testing/development), you will need to:
#. Create a virtualenv (basic).
#. Install application package as develop.
   .. code-block:: bash
        python setup.py develop
#. Serve the application itself:
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
        gunicorn {{ cookiecutter.project_slug }}.app:app --bind:127.0.0.1:8000 --reload

   Or
   
   .. code-block:: bash
        export FALCON_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.local
        python {{ cookiecutter.project_slug}}/app.py

It is very important to set the environment before serving the app or it won't work.

{% if cookiecutter.use_docker == "y" %}

Docker
^^^^^^

To tun docker container application you just need to run:
{% endif %}
