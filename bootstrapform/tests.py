import os
from distutils.version import StrictVersion

import django
from django.test import TestCase
from django.template import Template, Context
from django import forms


TEST_DIR = os.path.abspath(os.path.join(__file__, '..'))


CHOICES = (
    (0, 'Zero'), 
    (1, 'One'), 
    (2, 'Two'),
)

try:
    # required by Django 1.7 and later
    django.setup()
except:
    pass

class ExampleForm(forms.Form):
    char_field = forms.CharField()
    choice_field = forms.ChoiceField(choices=CHOICES)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    multiple_checkbox = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    file_fied = forms.FileField()
    password_field = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    boolean_field = forms.BooleanField()


class BootstrapTemplateTagTests(TestCase):
    maxDiff = None

    def test_basic_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap %}{{ form|bootstrap }}").render(Context({'form': form}))


        if StrictVersion(django.get_version()) >= StrictVersion('1.7'):
            fixture = 'basic.html'
        elif StrictVersion(django.get_version()) >= StrictVersion('1.6'):
            fixture = 'basic_dj16.html'
        else:
            fixture = 'basic_old.html'

        tpl = os.path.join('fixtures', fixture)
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)

    def test_horizontal_form(self):
        form = ExampleForm()

        html = Template("{% load bootstrap %}{{ form|bootstrap_horizontal }}").render(Context({'form': form}))

        if StrictVersion(django.get_version()) >= StrictVersion('1.7'):
            fixture = 'horizontal.html'
        elif StrictVersion(django.get_version()) >= StrictVersion('1.6'):
            fixture = 'horizontal_dj16.html'
        else:
            fixture = 'horizontal_old.html'
        
        tpl = os.path.join('fixtures', fixture)
        with open(os.path.join(TEST_DIR, tpl)) as f:
            content = f.read()

        self.assertHTMLEqual(html, content)
