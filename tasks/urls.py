from django.contrib import admin
from django.urls import path, include
from . import views


from django.conf.urls.static import  static
from django.conf import settings


urlpatterns = [
    path('', views.index),
    path('register', views.registration),
    #path('imagedeployment',views.ImageDeployment),
    path('imagedeployment',views.ImageDeployment),
    path('tasks',views.getTasks),
    path('taskstatus', views.taskStatus),
    path('clients', views.listClients),
    path('<str:mac>/',views.clientDetails),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)