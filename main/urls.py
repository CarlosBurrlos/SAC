from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.Home, name='homepage'),
    path('debugging/', views.debugging, name='debugging'),
    path('edit_counts/', views.EditCountsReport, name='editcountsreport'),
    path('edit_counts/<int:itemid>', views.UpdateCountReport, name='edititem'),
    path('view_report/', views.ViewReport, name='viewreport'),
    path('variancereport/', views.VarianceReportShower, name='variancereport'),
    path('update_count/<int:id>/<int:itemid>/', views.ActualUpdate, name='updateitem'),
]