from django.contrib import admin
from django import forms

from . import models
from .models import CustomUser

admin.site.site_header = "Epic Events Admin"
admin.site.site_title = "Epic Events"

admin.site.register(models.Customer)
admin.site.register(models.Event)
admin.site.register(models.Contract)


class CustomUserForm(forms.ModelForm):
    class Meta:
        """Meta options."""

        model = CustomUser
        fields = ("username", "password", "first_name", "last_name", "email", "role")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if self.cleaned_data.get("role") == 1:
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    form = CustomUserForm
    list_display = ("id", "username", "email", "role", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("role",)
