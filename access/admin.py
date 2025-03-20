from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from access.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

'''try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass'''

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    form = UserChangeForm 
    search_fields = ["email", "name", "bio"]
    readonly_fields = ["id", "uuid", "created_at", "updated_at"]

    list_display = [
        "email",
        "name",
        "bio",
        "is_active",
        "is_admin",
        "created_at",
    ]

    list_filter = [
        "is_active",
        "is_admin",
        "created_at",
    ]

    filter_horizontal = []

    date_hierarchy = "created_at"
    ordering = ["-created_at"]

    add_fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "email",
                    "name",
                    "bio",
                ]
            },
        ),
        (
            _("Access"),
            {"fields": ["is_active", "is_admin", "is_staff", "is_superuser"]},
        ),
    )

    fieldsets = (
        (
            _("Details"),
            {
                "fields": [
                    "id",
                    "uuid",
                    "email",
                    "name",
                    "bio",
                ]
            },
        ),
        (
            _("Access"),
            {
                "fields": [
                    "is_active",
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                    "password",
                ]
            },
        ),
        (_("Dates"), {"fields": ["created_at", "updated_at"]}),
    )

    class Media:
        pass
