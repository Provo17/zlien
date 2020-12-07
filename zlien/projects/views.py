from django.shortcuts import render
from django.contrib import messages
import csv, io
from .models import *

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
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Projects.objects.update_or_create(
            customer_name=column[0],
            project_name=column[1],
            project_address=column[2],
            project_city=column[3],
            project_state=column[4],
            project_zip=column[5],
            project_start_date=column[6],
            project_outstading_debt=column[7],
            project_commencement_date=column[8],
            order_type=column[9]
        )
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
