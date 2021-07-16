from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('blobtest/', views.blobTestIndex, name='blobtest')
]