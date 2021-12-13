"""
forms
"""
from app.account.models import AccountUser
from django import forms
from django.contrib.auth import get_user_model
<<<<<<< HEAD

from account.models import AccountUser
=======
>>>>>>> 12fe739 (Configuring containers.)


class AccountUserForm(forms.ModelForm):
    """
    Account user form
    """

    user = forms.ModelChoiceField(queryset=get_user_model().objects.filter(is_superuser=False))

    class Meta:
        model = AccountUser
        fields = ("user",)
