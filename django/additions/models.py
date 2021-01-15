from django.db import models
from django.shortcuts import reverse

from khrustaleva_show.utils import create_slug

class Addition(models.Model):
	name = models.CharField("название дополнения", max_length = 50)
	slug = models.SlugField("ссылка на дополнение", max_length = 50, unique = True)
	icon = models.ImageField("иконка дополнения", upload_to = "additions/icon")
	min_description = models.CharField("краткое описание дополнения", max_length = 170)
	description = models.TextField("описание дополнения")
	cost = models.PositiveSmallIntegerField("стоимость дополнения")
	part1 = models.CharField("пункт 1, входящий в дополнение", max_length = 50)
	part2 = models.CharField("пункт 2, входящий в дополнение", max_length = 50, blank = True)
	part3 = models.CharField("пункт 3, входящий в дополнение", max_length = 50, blank = True)
	part4 = models.CharField("пункт 4, входящий в дополнение", max_length = 50, blank = True)
	part5 = models.CharField("пункт 5, входящий в дополнение", max_length = 50, blank = True)
	part6 = models.CharField("пункт 6, входящий в дополнение", max_length = 50, blank = True)
	part7 = models.CharField("пункт 7, входящий в дополнение", max_length = 50, blank = True)
	photo1 = models.ImageField("фотография 1", upload_to = "additions/photo", blank = True)
	photo2 = models.ImageField("фотография 2", upload_to = "additions/photo", blank = True)
	photo3 = models.ImageField("фотография 3", upload_to = "additions/photo", blank = True)
	photo4 = models.ImageField("фотография 4", upload_to = "additions/photo", blank = True)
	photo5 = models.ImageField("фотография 5", upload_to = "additions/photo", blank = True)
	
	def get_absolute_url(self):
		return reverse('addition_block_detail_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = create_slug(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Дополнение"
		verbose_name_plural = "Дополнения"