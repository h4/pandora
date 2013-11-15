# coding=utf-8

from django.contrib import admin
from .models import *


class ThingAdmin(admin.ModelAdmin):
	list_display=['id', 'title', 'things_type', 'created', 'updated',]
	list_display_links=['title',]
	list_editable=['things_type',]


class ThingsTypeAdmin(admin.ModelAdmin):
	list_display=['id', 'title', 'created', 'updated',]
	fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Характеристики', {
            'fields': ( 'kind', 'color',)
        }),
    )

admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingsType, ThingsTypeAdmin)
