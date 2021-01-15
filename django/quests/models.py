from django.db import models
from django.shortcuts import reverse

from khrustaleva_show.utils import create_slug

class Quest(models.Model):
	name = models.CharField("название квеста", max_length = 50)
	slug = models.SlugField("ссылка на квест", max_length = 50, unique = True)
	image = models.ImageField("картинка квеста", upload_to = "quests/image")
	min_description = models.CharField("краткое описание", max_length = 170)
	description = models.TextField("описание")
	cost = models.PositiveSmallIntegerField("стоимость квеста")
	part1 = models.CharField("пункт 1, входящий в квест", max_length = 50)
	part2 = models.CharField("пункт 2, входящий в квест", max_length = 50, blank = True)
	part3 = models.CharField("пункт 3, входящий в квест", max_length = 50, blank = True)
	part4 = models.CharField("пункт 4, входящий в квест", max_length = 50, blank = True)
	part5 = models.CharField("пункт 5, входящий в квест", max_length = 50, blank = True)
	part6 = models.CharField("пункт 6, входящий в квест", max_length = 50, blank = True)
	part7 = models.CharField("пункт 7, входящий в квест", max_length = 50, blank = True)
	photo1 = models.ImageField('фотография 1', upload_to='quests/photo', blank=True)
	photo2 = models.ImageField('фотография 2', upload_to='quests/photo', blank=True)
	photo3 = models.ImageField('фотография 3', upload_to='quests/photo', blank=True)
	photo4 = models.ImageField('фотография 4', upload_to='quests/photo', blank=True)
	photo5 = models.ImageField('фотография 5', upload_to='quests/photo', blank=True)

	def get_absolute_url(self):
		return reverse('quest_block_detail_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = create_slug(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Квест"
		verbose_name_plural = "Квесты"