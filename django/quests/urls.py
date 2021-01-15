from django.urls import path

from . import views

urlpatterns = [
	path('<str:slug>/', views.questDetail, name = 'quest_block_detail_url'),
]