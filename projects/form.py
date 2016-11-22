import datetime
from django import forms
from django.forms import widgets

from projects.models import Project, ProjectStatus


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class':'form-control','required':'required'}
        self.fields['description'] = forms.CharField(widget=forms.Textarea)
        self.fields['description'].widget.attrs = {'class':'form-control'}
        self.fields['deadline'].widget.attrs = {'class': 'form-control datepicker'}
        self.fields['status'] = forms.ModelChoiceField(
        queryset=ProjectStatus.objects.all())
        self.fields['status'].widget.attrs = {'class':'form-control'}

    class Meta:
         model = Project
         fields = ['name', 'description','deadline','status']