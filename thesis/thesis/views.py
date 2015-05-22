from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

import logging
logger = logging.getLogger(__name__)

def home(request):
    response_page = 'home.html'
    return render_to_response(response_page, {

    }, context_instance = RequestContext(request))
