"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', 'thesis.views.home', name='home'),

    url(r'^subjects/$', 'thesis.views.subjects', name='subjects'),
    url(r'^services/$', 'thesis.views.services', name='services'),
    url(r'^teachers/$', 'thesis.views.teachers', name='teachers'),
    url(r'^essay/$', 'thesis.views.essay', name='essay'),
    url(r'^research_units/$', 'thesis.views.research_units', name='research_units'),
    url(r'^research_volume/$', 'thesis.views.research_volume', name='research_volume'),
    
    url(r'^admin/', include(admin.site.urls)),
]
