# encoding=utf-8
from django.db import models
from core.models import TimeStampedModel

kinds = (
	(u'1', u'Твёрдое'),
	(u'2', u'Жидкость'),
	(u'3', u'Газ'),
	)


class Thing(TimeStampedModel):
	"""
	Модель сущностей
	"""
	title = models.TextField('Название', max_length=32)
	things_type = models.ForeignKey('ThingsType', verbose_name=u'Тип')

	class Meta(object):
		verbose_name=u'Вещь'
		verbose_name_plural=u'Вещи'
		ordering = ['title',]

	def __unicode__(self):
		return u'{}, ({})'.format(self.title, self.things_type)

	def get_absolute_url(self):
		return u'things/{}/'.format(self.id)


class ThingsType(TimeStampedModel):
	"""
	Типы сущностей
	"""
	title = models.TextField('Название', max_length=32)
	kind = models.CharField('Состояние', max_length=2, choices=kinds)
	color = models.TextField('Цвет', max_length=32)

	class Meta(object):
		verbose_name=u'Тип вещей'
		verbose_name_plural=u'Типы вещей'

	def __unicode__(self):
		return u'{}'.format(self.title)
