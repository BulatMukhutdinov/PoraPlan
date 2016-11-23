from django import forms

from meetings.models import Meeting


class MeetingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget.attrs = {'class': 'form-control'}
        self.fields['meeting_type'].widget.attrs = {'class': 'form-control'}
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'My meeting', 'id': 'meeting_name'}
        self.fields['purpose'].widget.attrs = {'class': 'form-control', 'placeholder': 'Purpose of the Meeting',
                                               'id': 'meeting_purpose'}
        self.fields['subject'].widget.attrs = {'class': 'form-control',
                                               'placeholder': 'Identification of Subject matter',
                                               'id': 'meeting_subject'}
        self.fields['date'].widget.attrs = {'class': 'form-control', 'id': 'date'}

    class Meta:
        model = Meeting
        fields = ['name', 'project', 'meeting_type', 'date', 'purpose', 'subject']
