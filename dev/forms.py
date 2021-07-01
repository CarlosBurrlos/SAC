import django.forms
from django.db import connections
from django.db import models
from django.forms import Form
from django.forms import ModelForm

class uploadFileForm(Form):
    file = django.forms.FileField()
