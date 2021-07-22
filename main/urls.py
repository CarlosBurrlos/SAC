from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='homepage'),
    path('debugging/', views.debugging, name='debugging'),
    path('edit_counts/', views.editCountsReport, name='editcountsreport'),
    path('view_report/', views.viewReport, name='viewreport'),
    #path('edit_counts/<int:itemid>', views.)
]