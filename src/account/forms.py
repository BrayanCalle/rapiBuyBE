"""
forms
"""
from django import forms

from account.models import User


class UserForm(forms.ModelForm):
    """
    Account user form
    """

    user = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False))

    class Meta:
        model = User
        fields = ("user",)
