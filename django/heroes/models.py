from django.db import models
from django.shortcuts import reverse

from khrustaleva_show.utils import create_slug

class Hero(models.Model):
	name = models.CharField('имя героя', max_length = 200)
	slug = models.SlugField('ссылка на героя', max_length=50, unique = True)
	description = models.TextField('описание героя')
	cost = models.PositiveSmallIntegerField('стоимость героя')
	image = models.ImageField('изображение героя', upload_to='heroes/image')
	photo1 = models.ImageField('фотография 1', upload_to='heroes/photo', blank=True)
	photo2 = models.ImageField('фотография 2', upload_to='heroes/photo', blank=True)
	photo3 = models.ImageField('фотография 3', upload_to='heroes/photo', blank=True)
	photo4 = models.ImageField('фотография 4', upload_to='heroes/photo', blank=True)
	photo5 = models.ImageField('фотография 5', upload_to='heroes/photo', blank=True)


	def get_absolute_url(self):
		return reverse('hero_block_detail_url', kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = create_slug(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Герой"
		verbose_name_plural = "Герои"

