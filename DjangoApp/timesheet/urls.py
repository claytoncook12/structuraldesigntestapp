from django.urls import path
from timesheet import views

app_name='timesheet'
urlpatterns = [
    path('', views.timesheet_home, name='timesheet_home'),
    path('timesignin/', views.timesheet_signin, name='timesheet_signin'),
    path('timesignout/', views.timesheet_signout, name='timesheet_signout'),
    path('assignhours/', views.timesheet_assignhours, name='timesheet_assignhours'),
    path('checklist/', views.timesheet_checklist, name='timesheet_checklist'),
]
