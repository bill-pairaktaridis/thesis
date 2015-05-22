from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length = 200)
    rank = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 2000)
    link = models.CharField(max_length = 50)
    research_unit = models.ForeignKey('ResearchUnit', null = True, blank = True)

    def __unicode__(self):
        return "%s" % (self.name)

class ResearchUnit(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    def __unicode__(self):
        return "%s" % (self.title)
