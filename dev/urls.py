from django.urls import path
from . import views

# TODO :: Update the path URL's to accept regular expressions instead of strings

urlpatterns=[
    path('', views.index, name='index'),
    # Dev testing of local file upload
    path('localupload/', views.upload, name='upload'),
    path('uploadSuccess/', views.uploadSuccess, name='uploadSuccess'),
    # Dev testing of parsing operations
    path('testing/', views.testView, name='testView')
]
