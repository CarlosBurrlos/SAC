from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('uploadSuccess/', views.uploadSuccess, name='uploadSuccess'),
    path('localupload/', views.upload, name='upload')
]