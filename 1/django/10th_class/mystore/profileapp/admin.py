from django.contrib import admin
from .models import UserProfile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'video']
    search_fields = ['name']


admin.site.register(UserProfile, ProfileAdmin)
