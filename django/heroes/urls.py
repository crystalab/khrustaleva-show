from django.urls import path

from . import views

urlpatterns = [
	path('<str:slug>/', views.heroDetail, name = 'hero_block_detail_url'),
]