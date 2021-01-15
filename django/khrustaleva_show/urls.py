"""khrustaleva_show URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name = 'main_url'),
    path('program/', program , name = 'main_url'),
    path('standart_set/', standartSet, name = 'main_url'),
    path('vip_set/', vipSet, name = 'main_url'),
    path('super_set/', superSet, name = 'main_url'),
    path('assistance/', assistance, name = 'main_url'),
	path('heroes/', include('heroes.urls')),
    path('additions/', include('additions.urls')),
    path('shows/', include('shows.urls')),
    path('quests/', include('quests.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)