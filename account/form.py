from django import forms
from account.models import Account

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()


class AccountForm(forms.Form):

    class Meta:
        model = Account
        fields = ['avatar','company', 'position', 'birthday','phone','country','city','website']