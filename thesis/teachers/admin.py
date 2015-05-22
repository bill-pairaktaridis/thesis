from django.contrib import admin

from models import Teacher, ResearchUnit

# Register your models here.



class TeacherAdmin( admin.ModelAdmin ):
    list_display = ('name', 'rank', 'school')
    ordering = ('name',)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ResearchUnit)
