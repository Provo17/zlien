from django.db import models
from .custom_fields import ZipCodeField
import datetime

#Main projects class
class Projects(models.Model):
    order_type = [('Notice','Notice'),
                ('Lien','Lien')]
    customer_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    project_address = models.CharField(max_length=255)
    project_city = models.CharField(max_length=255)
    project_state = models.CharField(max_length=2)
    project_zip = ZipCodeField(max_value=5)
    project_start_date = models.DateField(auto_now=False)
    project_outstading_debt = models.DecimalField(blank=True, max_digits=20, decimal_places=2)
    project_commencement_date = models.DateField(blank=True, auto_now=False)
    order_type = models.CharField(max_length=255, blank=True, choices=order_type)

    @property
    def order_deadline(self):
        if self.order_type == 'Notice':
            if self.project_state == "TX":
                deadline = self.project_commencement_date + datetime.timedelta(15)
                return deadline
            deadline = self.project_commencement_date + datetime.timedelta(60)
            return deadline
        else:
            deadline = self.project_commencement_date + datetime.timedelta(90)
            return deadline

    def __str__(self):
        return self.customer_name
    class Meta:
        verbose_name = "Project"
