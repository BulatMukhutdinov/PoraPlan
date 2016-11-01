from django import forms

from meetings.models import Meeting


class MeetingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs = {'class': 'form-control'}
        self.fields['meeting_type'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Meeting
        fields = ['name', 'project', 'meeting_type', 'date']
