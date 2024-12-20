from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'email', 'role', 'preferences', 'groups', 'is_staff', 'is_active']
#     list_filter = ['role' ,'is_staff', 'is_active']

# Register CustomUser with the custom admin class
admin.site.register(CustomUser)
admin.site.register(StudyGroup)
admin.site.register(Preference)

# Register other models
admin.site.register(Notes)
