"""
forms
"""
from django import forms
from django.contrib.auth import get_user_model
from account.models import AccountUser


class AccountUserForm(forms.ModelForm):
    """
    Account user form
    """

    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.filter(is_superuser=False)
    )

    class Meta:
        model = AccountUser
        fields = ("user",)
