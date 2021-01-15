from django.urls import path

from . import views

urlpatterns = [
	path('<str:slug>/', views.showDetail, name = 'show_block_detail_url'),
]