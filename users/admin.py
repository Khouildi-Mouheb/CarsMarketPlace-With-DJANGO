from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields displayed in the user list in the admin panel
    list_display = ('username', 'email', 'phone_number', 'is_staff')

    # Add custom fields to the admin detail view
    # 'fieldsets' define sections in the user detail page
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'profile_picture', 'date_of_birth')}),
    )

    # Add custom fields to the admin create user form
    # 'add_fieldsets' define fields shown when creating a new user via the admin interface
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'phone_number', 'profile_picture', 'date_of_birth')}),
    )

