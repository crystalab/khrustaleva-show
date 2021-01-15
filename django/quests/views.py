from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Quest
from khrustaleva_show.utils import sendToTelegram

def questDetail(request, slug):
	quest = get_object_or_404(Quest, slug=slug)
	slug = quest.slug
	if request.method == 'GET':
		return render(request, 'quests/quest_detail.html', context={'quest': quest, 'slug': slug})
	elif request.method == 'POST':
		msg = '{0} оставил заявку на странице с квестом "{1}" ({2}{3}). Номер телефона: {4}'.format(request.POST['name'], quest.name, request.META['HTTP_HOST'], quest.get_absolute_url(), request.POST['tel'])
		sendToTelegram(msg)
		return render(request, 'quests/quest_detail.html', context={'quest': quest, 'slug': slug})