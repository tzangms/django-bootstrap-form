from django import forms

CHOICES = (
    (0, 'Zero'),
    (1, 'One'),
    (2, 'Two'),
)

class ExampleForm(forms.Form):
    char_field = forms.CharField()
    optional_char_field = forms.CharField(required=False)
    choice_field = forms.ChoiceField(choices=CHOICES)
    radio_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    multiple_choice = forms.MultipleChoiceField(choices=CHOICES)
    multiple_checkbox = forms.MultipleChoiceField(
        choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    file_fied = forms.FileField()
    password_field = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    boolean_field = forms.BooleanField()
    optional_boolean_field = forms.BooleanField(required=False)
