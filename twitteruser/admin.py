from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'displayname',
                    
                ),
            },
        ),
    )

admin.site.register(models.TwitterUserModel, CustomUserAdmin)


