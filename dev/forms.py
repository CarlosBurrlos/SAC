from django import forms
from .widgets import ClearableMultipleFilesInput
from .fields import MultipleFilesField
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

class upload(forms.Form):
    upload = MultipleFilesField(
        widget=ClearableMultipleFilesInput(
            attrs={'multiple': True}
        )
    )
