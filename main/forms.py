from django import forms
from .models import PolicyProcedures, EditcountsqtyVariance

PolicyChoices = [
    ('A', 'A'),
    ('NA', 'NA'),
    ('UA', 'UA')
]

class UpdateItem(forms.ModelForm):
    accepted = forms.BooleanField(required=False, initial=True)
    class Meta:
        model = EditcountsqtyVariance
        fields = ['currentcount', 'accepted']

class PolicyStatement(forms.ModelForm):
    fieldname = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    compliance_level = forms.CharField(widget=forms.Select(choices=PolicyChoices))
    notes = forms.CharField(required=False)
    auditid = forms.IntegerField(widget=forms.HiddenInput())
    correctivetext = forms.CharField(widget=forms.HiddenInput())
    pointvalues = forms.IntegerField(widget=forms.HiddenInput())
    storeid = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = PolicyProcedures
        fields = ['fieldname', 'compliance_level', 'notes', 'auditid', 'correctivetext', 'pointvalues','storeid']