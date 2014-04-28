import django
from django import forms, VERSION as django_version
from django.template import Context
from django.template.loader import get_template
from django import template

from bootstrapform import config

register = template.Library()

@register.filter
def bootstrap(element):
    markup_classes = {'label': '', 'value': '', 'single_value': ''}
    return render(element, markup_classes)


@register.filter
def bootstrap_inline(element):
    markup_classes = {'label': 'sr-only', 'value': '', 'single_value': ''}
    return render(element, markup_classes)


@register.filter
def bootstrap_horizontal(element, label_cols=None):
    if not label_cols:
        label_cols = config.BOOTSTRAP_LABEL_COLS

    markup_classes = {'label': label_cols, 'value': '', 'single_value': ''}

    # Extract each class of label column to compute class of column value
    for css_class in label_cols.split(' '):
        # Eg. 'col-sm-2'
        label_class = css_class.split('-')

        try:
            label_nb_cols = int(label_class[-1])
        except ValueError:
            label_nb_cols = None

        if label_nb_cols is None or label_nb_cols >= config.BOOTSTRAP_COLUMN_COUNT:
            label_nb_cols = config.BOOTSTRAP_DEFAULT_VALUE_COLUMN_COUNT

        value_nb_cols = config.BOOTSTRAP_COLUMN_COUNT - label_nb_cols
        value_offset_class = "%s-%s-offset-%d" % (label_class[0], label_class[1], label_nb_cols)
        value_class = "%s-%s-%d" % (label_class[0], label_class[1], value_nb_cols)

        markup_classes['single_value'] += " %s %s" % (value_offset_class, value_class)
        markup_classes['value'] += " %s" % value_class

    return render(element, markup_classes)

@register.filter
def add_input_classes(field):
    if not is_checkbox(field) and not is_multiple_checkbox(field) \
       and not is_radio(field) and not is_file(field):
        field_classes = field.field.widget.attrs.get('class', '')
        field_classes += ' form-control'
        field.field.widget.attrs['class'] = field_classes


def render(element, markup_classes):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        add_input_classes(element)
        template = get_template("bootstrapform/field.html")
        context = {'field': element, 'classes': markup_classes, 'form': element.form}
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    add_input_classes(field)

            template = get_template("bootstrapform/formset.html")
            context = {'formset': element, 'classes': markup_classes}
        else:
            for field in element.visible_fields():
                add_input_classes(field)

            template = get_template("bootstrapform/form.html")
            context = {'form': element, 'classes': markup_classes}


    if django_version < (1, 8):
        context = Context(context)

    return template.render(context)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)
