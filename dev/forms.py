from django import forms
from django.forms import ClearableFileInput
from .models import UploadFile

class UploadFileForm(forms.ModelForm):
    class meta:
        model = UploadFile
        fields = ['files']
        widgets = {
            'files': ClearableFileInput(attrs={'multiple': True})
        }



class uploadFileForm(forms.Form):
    upload = forms.FileField()
