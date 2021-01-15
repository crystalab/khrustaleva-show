from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Show
from khrustaleva_show.utils import sendToTelegram

def showDetail(request, slug):
	show = get_object_or_404(Show, slug=slug)
	slug = show.slug
	if request.method == 'GET':
		return render(request, 'shows/show_detail.html', context={'show': show, 'slug': slug})
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на странице с шоу "{1}" ({2}{3}). Номер телефона: {4}'.format(request.POST['name'], show.name, request.META['HTTP_HOST'], show.get_absolute_url(), request.POST['tel'])
		sendToTelegram(msg)
		return render(request, 'shows/show_detail.html', context={'show': show, 'slug': slug})