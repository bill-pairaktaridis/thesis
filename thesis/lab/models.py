from django.db import models

# Create your models here.

class Lab(models.Model):
    title = models.CharField(max_length = 50)
    school = models.CharField(max_length = 100)
    
    research_objects = models.CharField(max_length = 500)
    services = models.CharField(max_length = 500)

    essay = models.CharField(max_length = 2000)

    def __unicode__(self):
        return "%s" % (self.title)
