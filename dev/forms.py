import django.forms
from django.forms import Form
from django import forms
from django.forms import ModelForm
from .models import EditcountsqtyVariance, PolicyProcedures
from .models import uploadFileTestModel
from django.forms import modelformset_factory

PolicyChoices = [
    (10, 'A'),
    (10, 'NA'),
    (0, 'UA')
]

class uploadFileForm(Form):
    file = django.forms.FileField()

class uploadFileModelForm(ModelForm):

    class Meta:
        model = uploadFileTestModel
        fields = ['file']

class UpdateItem(ModelForm):
    accepted = forms.BooleanField(required=False, initial=True)
    class Meta:
        model = EditcountsqtyVariance
        fields = ['currentcount', 'accepted']

class PolicyStatement(forms.ModelForm):
    fieldname = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    compliance_level = forms.IntegerField(widget=forms.Select(choices=PolicyChoices))
    notes = forms.CharField(required=False)
    auditid = forms.IntegerField(widget = forms.HiddenInput())
    storeid = forms.IntegerField(widget = forms.HiddenInput())

    class Meta:
        model = PolicyProcedures
        fields = ['fieldname', 'compliance_level', 'notes', 'auditid', 'storeid']