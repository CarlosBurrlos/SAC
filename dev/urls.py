from django.urls import path
from django.urls import re_path
from . import views

# TODO :: Update the path URL's to accept regular expressions instead of strings

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('', views.index, name='index'),
    re_path(r'(?i)^sac/$', views.SAC, name='sac'),
    path('edit_counts/', views.EditCountsReport, name='editcounts'),
    re_path(r'(?i)^export_audit/$', views.EXPORTAUDIT, name='exportaudit'),
##    re_path(r'(?i)^report/$', views.REPORT, name='report'),
    path('edit_count/<int:itemid>', views.UpdateCountReport, name='edititem'),
    path('updated_count/<int:id>/<int:itemid>/', views.ActualUpdate, name='updateitem'),
    path('report/', views.AuditReportViewer, name='reportresults'),
    path('update_violation/', views.ActualUpdateViolation, name='updateviolation'),
    path('extra_reports/', views.ExtraReports, name='extrareports'),
    path('top50shrink/', views.Top50Shrink, name='top50shrink'),
    path('skusnotcounted/', views.SkusNotCounted, name='skusnotcounted'),
    path('departmentvariance/', views.DepartmentVariance, name='departmentvariance'),
    path('cartonsummary/', views.CartonSummary, name='cartonsummary'),
    path('cartondetail/<str:cartonid>', views.CartonDetail, name='cartondetail')
]
