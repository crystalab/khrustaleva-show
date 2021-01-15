from django.db import models

class Images(models.Model):
	image = models.ImageField('фотография', upload_to = 'gallery/image')

	class Meta:
		verbose_name = "фотография"
		verbose_name_plural = "Фотографии"