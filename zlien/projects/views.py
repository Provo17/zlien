from django.shortcuts import render
from django.contrib import messages
import csv, io, datetime
from .models import *
from .functions import csv_upload

def project_upload(request):
    # declaring template
    template = "index.html"

    #Queryset to return all project objects
    data = Projects.objects.all()
    # prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be Customer name, project name, project address, project city, project state, project zip, project start date (YYYY-MM-DD), project outstanding debt, project commencement date (YYYY-MM-DD), order type',
        'profiles': data
    }
    csv_upload(request, template, prompt)
    context = {}
    return render(request, template, context)



def project_listing(request):
    # declaring template
    template = "project_list.html"

    #Queryset to return all project objects
    projects = list(Projects.objects.all())

    #Sends queryset to template
    context = {
        'projects': projects,
    }

    return render(request, template, context)
