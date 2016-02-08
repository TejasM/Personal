# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template


def learnings(request, slug):
	file_name = (slug.replace('-', '_') + '.html').lower()
	try:
		t = get_template('learnings/' + file_name)
	except:
		raise Http404("Sorry no such page exists")
	return render(request, 'learnings/' + file_name)

def projects(request, slug):
	file_name = (slug.replace('-', '_') + '.html').lower()
	try:
		t = get_template('projects/' + file_name)
	except:
		raise Http404("Sorry no such page exists")
	return render(request, 'projects/' + file_name)

def writings(request, slug):
	file_name = (slug.replace('-', '_') + '.html').lower()
	try:
		t = get_template('writings/' + file_name)
	except:
		raise Http404("Sorry no such page exists")
	return render(request, 'writings/' + file_name)
