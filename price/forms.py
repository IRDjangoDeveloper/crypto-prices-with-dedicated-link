from django import forms

Choice = (
    ('bitcoin', 'Bitcoin',),
    ('dogecoin', 'Dogecoin',),
)
class Userrequest(forms.Form):
    coin = forms.ChoiceField(choices=Choice, widget=forms.Select(attrs={'class':'form-control'}))