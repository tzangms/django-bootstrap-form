from django.template import Context
from django.template.loader import get_template
from django import template

register = template.Library()


@register.filter
def bootstrap(element):
    element_type = element.__class__.__name__.lower()

    if element_type == 'boundfield':
        classes = element.field.widget.attrs.get('class', '')
        classes += ' form-control'
        element.field.widget.attrs['class'] = classes

        template = get_template("bootstrapform/field.html")
        context = Context({'field': element})
    else:
        has_management = getattr(element, 'management_form', None)
        if has_management:
            for form in element.forms:
                for field in form.visible_fields():
                    classes = field.field.widget.attrs.get('class', '')
                    classes += ' form-control'
                    field.field.widget.attrs['class'] = classes

            template = get_template("bootstrapform/formset.html")
            context = Context({'formset': element})
        else:
            for field in element.visible_fields():
                classes = field.field.widget.attrs.get('class', '')
                classes += ' form-control'
                field.field.widget.attrs['class'] = classes

            template = get_template("bootstrapform/form.html")
            context = Context({'form': element})

    return template.render(context)


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__.lower() == "checkboxinput"


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__.lower() == "radioselect"
