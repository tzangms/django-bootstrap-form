=======================
Django Semantic UI form
=======================

.. image:: https://badge.fury.io/py/django-semanticui-form.png
   :alt: PyPI version
   :target: https://pypi.python.org/pypi/django-semanticui-form

.. image:: https://travis-ci.org/peterbe/django-semanticui-form.png?branch=master
    :target: https://travis-ci.org/peterbe/django-semanticui-form

.. image:: https://coveralls.io/repos/peterbe/django-semanticui-form/badge.png?branch=master
   :target: https://coveralls.io/r/peterbe/django-semanticui-form?branch=master


Semantic UI for Django Form.

A simple Django template tag to work with `Semantic UI <http://semantic-ui.com/>`_

This project is a fork from
`django-bootstrap-form <https://github.com/tzangms/django-bootstrap-form>`_ by
`tzangms <https://github.com/tzangms>`_.

Usage
======

Add ``semanticuiform`` to your ``INSTALLED_APPS``.

At the top of your template load in our template tags::

	{% load semanticui %}

Then to render your form::

	<form class="ui form">
	    <legend>Form Title</legend>
	    {% csrf_token %}
	    {{ form|semanticui }}
        <button class="ui button" type="submit">Submit</button>
	</form>

To make the form with inline element, change the ``|semanticui`` template
tag to ``|semanticui_inline``.

	<form class="ui form">
	    <legend>Form Title</legend>
	    {% csrf_token %}
	    {{ form|semanticui_inline }}
        <button class="ui button" type="submit">Submit</button>
	</form>


Demo
=====

Not yet.
