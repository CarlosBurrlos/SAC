from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginTest, name='logintest'),
    path('upload/', views.upload, name='upload'),
    path('blobtest/', views.blobTestIndex, name='blobtest')
]