import datetime
from django import forms
from django.forms import widgets

from projects.models import Project


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class':'form-control','required':'required'}
        self.fields['description'] = forms.CharField(widget=forms.Textarea)
        self.fields['description'].widget.attrs = {'class':'form-control'}
        self.fields['deadline'].widget.attrs = {'class': 'form-control'}
        #self.fields['deadline'] = forms.DateField(initial=datetime.date.today)

    class Meta:
         model = Project
         fields = ['name', 'description','deadline']