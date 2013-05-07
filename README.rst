=====================
Django bootstrap form
=====================

Generate twitter-bootstrap form output for django form

A simple Django template tag to work with twitter bootstrap ( http://twitter.github.com/bootstrap/ )

`readthedocs <https://django-bootstrap-form.readthedocs.org/en/latest/>`_


Screenshot
-----------

.. image:: _static/example.png


Installation
------------

Install django-bootstrap-form with pip

.. code-block:: sh

    $ pip install django-bootstrap-form




Configuration
-------------

Add 'bootstrapform' to INSTALLED_APPS.

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bootstrapform',
        ...
    )


Usage
------

.. code-block:: none

    {% load bootstrap %}

    {{ form|bootstrap }}

    # or use with individual field

    {{ form.<field name>|bootstrap }} - To output individual fields

CHANGELOG
---------

- 2013-5-7:

  Add `radio` support for ChoiceField
