from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import redirect

from shares.models import Share
from heroes.models import Hero
from additions.models import Addition
from shows.models import Show
from quests.models import Quest
from gallery.models import Images
from .utils import sendToTelegram

def main(request):
	if request.method == 'GET':
		allShares = Share.objects.order_by('end_date')
		activeShares = [i for i in allShares if i.isActive()]
		heroes = Hero.objects.all()
		additions = Addition.objects.all()
		shows = Show.objects.all()
		quests = Quest.objects.all()
		images = Images.objects.all()
		return render(request, 'index.html', context = {'shares': activeShares, 'heroes': heroes, 'additions': additions, 'shows': shows, 'quests': quests, 'images': images})
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на главной странице сайта. Номер телефона: {1}'.format(request.POST['name'], request.POST['telephone'])
		sendToTelegram(msg)
		return redirect('/')

def program(request):
	if request.method == 'GET':
		return redirect('/')
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на главной странице сайта, во время просмотра блока с программой аниматора. Номер телефона: {1}'.format(request.POST['name'], request.POST['tel'])
		sendToTelegram(msg)
		return redirect('/')

def standartSet(request):
	if request.method == 'GET':
		return redirect('/')
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на главной странице сайта, во время просмотра стандартного пакета. Номер телефона: {1}'.format(request.POST['name'], request.POST['tel'])
		sendToTelegram(msg)
		return redirect('/')	
		
def vipSet(request):
	if request.method == 'GET':
		return redirect('/')
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на главной странице сайта, во время просмотра вип пакета. Номер телефона: {1}'.format(request.POST['name'], request.POST['tel'])
		sendToTelegram(msg)
		return redirect('/')	

def superSet(request):
	if request.method == 'GET':
		return redirect('/')
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на главной странице сайта, во время просмотра супер пакета. Номер телефона: {1}'.format(request.POST['name'], request.POST['tel'])
		sendToTelegram(msg)
		return redirect('/')	

def assistance(request):
	if request.method == 'GET':
		return redirect('/')
	elif request.method == 'POST':
		msg = '{0} оставил(а) заявку на звонок от консультанта. Номер телефона: {1}'.format(request.POST['name'], request.POST['tel'])
		sendToTelegram(msg)
		return redirect('/')		