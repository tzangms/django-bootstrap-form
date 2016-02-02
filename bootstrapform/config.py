from django.conf import settings

BOOTSTRAP_COLUMN_COUNT = getattr(settings, 'BOOTSTRAP_COLUMN_COUNT', 12)
BOOTSTRAP_FIELD_TEMPLATE = getattr(settings, 'BOOTSTRAP_FIELD_TEMPLATE', 'bootstrapform/field.html')
BOOTSTRAP_FORMSET_TEMPLATE = getattr(settings, 'BOOTSTRAP_FORMSET_TEMPLATE', 'bootstrapform/formset.html')
BOOTSTRAP_FORM_TEMPLATE = getattr(settings, 'BOOTSTRAP_FORM_TEMPLATE', 'bootstrapform/form.html')
