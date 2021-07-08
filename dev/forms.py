import django.forms
from django.db import connections
from django.db import models
from django.forms import Form
from django import forms
from django.forms import ModelForm
from .models import EditcountsqtyVariance

class uploadFileForm(Form):
    file = django.forms.FileField()


from .models import uploadFileTestModel

class uploadFileModelForm(ModelForm):
    class Meta:
        model = uploadFileTestModel
        fields = ['file']

class UpdateItem(ModelForm):

    accepted = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = EditcountsqtyVariance
        fields = ['currentcount', 'accepted']