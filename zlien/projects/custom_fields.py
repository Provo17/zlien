from django.db import models

#Custom field to impose a 5 int limit for zip code. By default Django ignores int limits when using the integer field.
class ZipCodeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, max_value=None, **kwargs):
        self.max_value = max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'max_value':self.max_value}
        defaults.update(kwargs)
        return super(ZipCodeField, self).formfield(**defaults)
