from django import forms

class ChoiceForm(forms.Form):
    choice1 = forms.fields.ChoiceField(
        required=True,
        widget=forms.widgets.Select
    )