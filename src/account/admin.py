"""
admin
"""
from tokenize import group
from django.contrib import admin

from account.models import Account, Location, UserNuevo


from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError




class LocationInline(admin.TabularInline):
    """
    Inline location
    """

    model = Location
    verbose_name = "Local"
    verbose_name_plural = "Locales"
    fields = ("name", "phone_number", "street_address", "email", "city")


class AccountAdmin(admin.ModelAdmin):
    """
    Admin Account
    """

    list_display = ("name", "acronym")
    search_fields = ("name", "acronym")
    list_filter = ("name", "acronym")
    fieldsets = ((("Información de Cuenta"), {"fields": ("name", "acronym")}),)
    inlines = (LocationInline,)


# Prueba

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    # username = forms.CharField(max_length=50, label="Username")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserNuevo
        fields = ('email','username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserNuevo
        fields = ('email', 'password', 'is_active', 'is_staff')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_staff', 'username')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        # ('Personal info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('groups','is_staff','is_active','is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()





admin.site.register(Account, AccountAdmin)
# Prueba
admin.site.register(UserNuevo, UserAdmin)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass
