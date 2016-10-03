from django import forms
import datetime
from django.db import connection

class EventsForm(forms.Form):
    tag = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255)
    time = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'], widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),initial=datetime.date.today)
    #expiration = forms.DateTimeField(widget=forms.widgets.DateTimeInput(input_formats=["%d %b %Y %H:%M:%S %Z"]))
    expiration = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'],widget=forms.DateTimeInput(attrs={'class':'form-control','type':'datetime-local'}),initial=datetime.date.today)
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=1024)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),max_length=255)

#    class Meta:
#        managed = False
#        db_table = 'Events'