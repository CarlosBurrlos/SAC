from django.urls import path
from . import views

# TODO :: Update the path URL's to accept regular expressions instead of strings

urlpatterns=[
    path('', views.index, name='index'),
    path('uploadSuccess/', views.uploadSuccess, name='uploadSuccess'),
    path('localupload/', views.upload, name='upload')
]