from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Addition
from khrustaleva_show.utils import sendToTelegram

def additionDetail(request, slug):
	addition = get_object_or_404(Addition, slug=slug)
	slug = addition.slug
	if request.method == 'GET':
		return render(request, 'additions/additions_detail.html', context={'addition': addition, 'slug': slug})
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на странице с персонажем "{1}" ({2}{3}). Номер телефона: {4}'.format(request.POST['name'], addition.name, request.META['HTTP_HOST'], addition.get_absolute_url(), request.POST['tel'])
		sendToTelegram(msg)
		return render(request, 'additions/additions_detail.html', context={'addition': addition, 'slug': slug})