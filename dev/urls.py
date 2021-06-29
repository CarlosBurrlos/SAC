from django.urls import path
from django.urls import re_path
from . import views

# TODO :: Update the path URL's to accept regular expressions instead of strings

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?i)^sac/$', views.SAC, name='sac'),
    re_path(r'(?i)^edit_counts/$', views.EDITCOUNTS, name='editcounts'),
    re_path(r'(?i)^export_audit/$', views.EXPORTAUDIT, name='exportaudit'),
    re_path(r'(?i)^process_audit/$', views.PROCESSAUDIT, name='processaudit'),
    re_path(r'(?i)^report/$', views.REPORT, name='report')
]
