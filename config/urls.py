# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.views.generic import TemplateView
from filebrowser.sites import site

from tejas.pages import views

urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name="home"),
                  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
                  url(r'^learnings/$', TemplateView.as_view(template_name='pages/learnings.html'), name="learnings"),
                  url(r'^projects/$', TemplateView.as_view(template_name='pages/projects.html'), name="projects"),
                  url(r'^writings/$', TemplateView.as_view(template_name='pages/writings.html'), name="writings"),

                  url(r'^learnings/(?P<slug>[\w-]+)/$', views.learnings, name='learnings_detail'),
                  url(r'^projects/(?P<slug>[\w-]+)/$', views.projects, name='projects_detail'),
                  url(r'^writings/(?P<slug>[\w-]+)/$', views.writings, name='writings_detail'),

                  # Django Admin, use {% url 'admin:index' %}
                  url(r'^admin/filebrowser/', include(site.urls)),
                  url(r'^grappelli/', include('grappelli.urls')),
                  url(settings.ADMIN_URL, include(admin.site.urls)),

                  # User management
                  url(r'^users/', include("tejas.users.urls", namespace="users")),
                  url(r'^accounts/', include('allauth.urls')),

                  # Your stuff: custom urls includes go here

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permissin Denied")}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
        url(r'^500/$', default_views.server_error),
    ]
