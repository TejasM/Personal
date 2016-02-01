# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin


def learnings(request, slug):
	pass

def projects(request, slug):
	pass

def writings(request, slug):
	file_name = (slug.replace('-', '_') + '.html').lower()
	try:
		t = get_template('writings/' + file_name)
	except:
		raise Http404("Sorry no such page exists")
	return render(request, 'writings/' + file_name)