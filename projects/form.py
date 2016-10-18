from django import forms
from projects.models import Project


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class':'form-control','required':'required'}
        self.fields['description'] = forms.CharField(widget=forms.Textarea)
        self.fields['description'].attrs = {'class':'form-control'}

    class Meta:
         model = Project
         fields = ['name', 'description']