import re
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
def bootstrap_horizontal(element, label_cols='col-sm-2 col-lg-2'):

    markup_classes = {'label': label_cols, 'value': '', 'single_value': ''}

    for cl in label_cols.split(' '):
        splitted_class = cl.split('-')

        try:
            value_nb_cols = int(splitted_class[-1])
        except ValueError:
            value_nb_cols = config.BOOTSTRAP_COLUMN_COUNT

        if value_nb_cols >= config.BOOTSTRAP_COLUMN_COUNT:
            splitted_class[-1] = config.BOOTSTRAP_COLUMN_COUNT
        else:
            offset_class = cl.split('-')
            offset_class[-1] = 'offset-' + str(value_nb_cols)
            splitted_class[-1] = str(config.BOOTSTRAP_COLUMN_COUNT - value_nb_cols)
            markup_classes['single_value'] += ' ' + '-'.join(offset_class)
            markup_classes['single_value'] += ' ' + '-'.join(splitted_class)

        markup_classes['value'] += ' ' + '-'.join(splitted_class)

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


# {% bootstrap %} tag

@register.tag(name='bootstrap')
def bootstrap_tag(parser, token):
    nodelist = parser.parse(('endbootstrap',))
    try:
        # Splitting by None == splitting by spaces.
        tag_name, form = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a form arguments" % token.contents.split()[0]
        )
    parser.delete_first_token()
    return Bootstrap(nodelist, form)


class Bootstrap(template.Node):
    def __init__(self, nodelist, form):
        self.nodelist = nodelist
        self.form_variable = form
    
    def render(self, context):
        tag_contents = self.nodelist.render(context)
        self.form = context[self.form_variable]
        return ''.join(self._get_rows(tag_contents))

    def _get_rows(self, tag_contents):
        for row in self._parse_fields(tag_contents):
            output = [
                '<div class="row">',
                ''.join(self._get_fields(row)),
                '</div>',
            ]
            yield ''.join(output)

    def _get_fields(self, row):
        for f, size in row:
            col_class = 'col'
            if size:
                col_class += '-md-' + size
            try:
                f = self.form[f]
            except KeyError as e:
                raise Exception('Failed to process line\n{}\n{}'.format(row, e))
            yield '<div class="{}">{}</div>'.format(col_class, bootstrap(f))
    
    def _parse_fields(self, tag_contents):
        result = []
        for line in tag_contents.splitlines():
            line = line.strip()
            if not line:
                continue
            field_names = [i.strip() for i in line.split(' ') if i.strip()]
            row = []
            for name in field_names:
                if '(' in name:
                    name, col_size = re.findall(r'^(.*?)\((\d+)\)$', name)[0]
                else:
                    col_size = None
                row.append((name, col_size))
            result.append(row)
        return result
