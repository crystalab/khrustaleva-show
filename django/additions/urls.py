from django.urls import path

from . import views

urlpatterns = [
	path('<str:slug>/', views.additionDetail, name = 'addition_block_detail_url'),
]