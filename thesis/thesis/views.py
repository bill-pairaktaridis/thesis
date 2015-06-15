from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

import logging
logger = logging.getLogger(__name__)

def home(request):
    response_page = 'home.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))

def subjects(request):
    response_page = 'subjects.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))

def services(request):
    response_page = 'services.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))

def teachers(request):
    from teachers.models import Teacher

    teachers = Teacher.objects.all()

    response_page = 'teachers.html'
    return render_to_response(response_page, {
        'teachers': teachers
    }, context_instance = RequestContext(request))

def essay(request):
    response_page = 'essay.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))

def research_units(request):
    from teachers.models import ResearchUnit

    units = ResearchUnit.objects.all()

    response_page = 'research_units.html'
    return render_to_response(response_page, {
                              'units': units,

    }, context_instance = RequestContext(request))

def research_volume(request):
    response_page = 'research_volume.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))
