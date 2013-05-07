from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField()
    choices = forms.ChoiceField(choices=((0, 'Zero'), (1, 'One'), (2, 'Two')), widget=forms.RadioSelect)
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
