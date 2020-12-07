from django.contrib import admin

'''
 This file registers the project class to the Django admin to use cms functionality.
'''

from .models import *

class ProjectsAdmin(admin.ModelAdmin):
    #Defines what fields will display in the django admin list view.
    list_display = ('customer_name', 'project_name', 'project_start_date', 'project_commencement_date')

    #Defines which fields will be clickable to view the individual record.
    list_display_links = ('customer_name',)

admin.site.register(Projects, ProjectsAdmin)
