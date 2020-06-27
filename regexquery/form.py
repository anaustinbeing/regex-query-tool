from django import forms

class RegexForm(forms.Form):
    string_input = forms.CharField(label='String', max_length=500)
    regex_input = forms.CharField(label='Regex', max_length=200)
    