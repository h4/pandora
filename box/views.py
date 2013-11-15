# encoding=utf-8

from django.shortcuts import render
from .models import Thing, ThingsType


def list(request):
	"""
	Список всех сущностей
	"""
	things = Thing.objects.order_by('title')
	context = {
		"things": things
	}

	return render(request, 'list.html', context)


def item(request, id):
	"""
	Страница отдельной сущности
	"""
	thing = Thing.objects.get(id=id)

	context = {
		"thing": thing,
	}

	return render(request, 'item.html', context)


def new_items(request):
	"""
	Список последних сущностей
	"""
	things = Thing.objects.order_by("-updated")[:3]

	context = {
		"things": things,
	}

	return render(request, 'list.html', context)
