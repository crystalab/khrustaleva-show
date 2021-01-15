from datetime import timedelta
from django.db import models
from django.utils import timezone


class Share(models.Model):
	name = models.CharField('название акции', max_length = 150)
	description = models.TextField('описание акции')
	end_date = models.DateTimeField('дата окончания')

	def isActive(self):
		return self.end_date > timezone.now()

	def minuteWord(self, minute):
		if minute % 10 > 4 or minute % 10 == 0 or minute // 10 == 1:
			return 'минут'
		elif minute % 10 == 1:
			return 'минута'
		else:
			return 'минуты'

	def hourWord(self, hour):
		if hour % 10 > 4 or hour % 10 == 0 or hour // 10 == 1:
			return 'часов'
		elif hour % 10 == 1:
			return 'час'
		else:
			return 'часа'

	def dayWord(self, day):
		if day % 10 > 4 or day % 10 == 0 or day // 10 == 1:
			return 'дней'
		elif day % 10 == 1:
			return 'день'
		else:
			return 'дня'

	def endDateString(self):
		if self.end_date - timedelta(seconds = 3600) < timezone.now():
			minute = (self.end_date - timezone.now()).seconds // 60 % 60
			return 'осталось {0} {1}'.format(minute, self.minuteWord(minute))
		elif self.end_date - timedelta(days = 1) < timezone.now():
			hour = (self.end_date - timezone.now()).seconds // 3600
			return 'осталось {0} {1}'.format(hour, self.hourWord(hour))
		elif self.end_date - timedelta(days = 14) < timezone.now():
			day = (self.end_date - timezone.now()).days
			return 'осталось {0} {1}'.format(day, self.dayWord(day)) 
		return 'до {0}'.format(share.end_date.strftime("%d.%m.%Y"))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Акция"
		verbose_name_plural = "Акции"
