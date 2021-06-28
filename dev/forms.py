from django import forms


class uploadFileForm(forms.Form):
    upload = forms.FileField()
