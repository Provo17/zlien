from django.contrib import admin

# Register your models here.

from .models import *

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'project_name',)
    list_display_links = ('customer_name',)

admin.site.register(Projects, ProjectsAdmin)
