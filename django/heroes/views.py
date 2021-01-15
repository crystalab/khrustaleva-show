from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Hero
from khrustaleva_show.utils import sendToTelegram

def heroDetail(request, slug):
	hero = get_object_or_404(Hero, slug=slug)
	slug = hero.slug
	if request.method == 'GET':
		return render(request, 'heroes/hero_detail.html', context={'hero': hero, 'slug': slug})
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на странице с дополнением "{1}" ({2}{3}). Номер телефона: {4}'.format(request.POST['name'], hero.name, request.META['HTTP_HOST'], hero.get_absolute_url(), request.POST['tel'])
		sendToTelegram(msg)
		return render(request, 'heroes/hero_detail.html', context={'hero': hero, 'slug': slug})