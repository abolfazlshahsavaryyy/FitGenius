# accounts/admin.py
from django.contrib import admin
from .models import ApplicationUser, Profile
from django.contrib.auth.admin import UserAdmin
# accounts/admin.py

class ApplicationUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role']

admin.site.register(ApplicationUser, ApplicationUserAdmin)

admin.site.register(Profile)
