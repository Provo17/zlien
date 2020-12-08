'''
This file contains fuctions to be used accross the application.
'''
import csv, io, datetime
from .models import *
from django.shortcuts import render
#This file contains fuctions to be used accross the application.

# This is the csv upload function
def csv_upload(request, template, prompt):
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
        #Check if commencement date is blank, if so, add today's date
        if column[8] == '':
            column[8] = datetime.datetime.now()
        #check if all other colums are present, only upload those that are.
        if all(column):
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
