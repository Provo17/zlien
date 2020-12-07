from django.db import models

# Create your models here.


#Custom field to impose a 5 int limit for zip code
class ZipCodeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, max_value=None, **kwargs):
        self.max_value = max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'max_value':self.max_value}
        defaults.update(kwargs)
        return super(ZipCodeField, self).formfield(**defaults)

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


    def __str__(self):
        return self.customer_name
    class Meta:
        verbose_name = "Project"
