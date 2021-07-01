from django.urls import path
from django.urls import re_path
from . import views

# TODO :: Update the path URL's to accept regular expressions instead of strings

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('', views.index, name='index'),
    re_path(r'(?i)^sac/$', views.SAC, name='sac'),
    re_path(r'(?i)^edit_counts/$', views.EditCountsReport, name='editcounts'),
    re_path(r'(?i)^export_audit/$', views.EXPORTAUDIT, name='exportaudit'),
    re_path(r'(?i)^report/$', views.REPORT, name='report'),
    path('snapreport/', views.Showemp, name='snapreport'),
    path('variancereport/', views.VarianceReportShower, name='variancereport'),
]
