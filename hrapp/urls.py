from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='departments'),
    path('departments/<int:department_id>', department_details, name='department'),
    path('programs/', program_list, name='program_list'),
    path('programs/form', program_form, name='program_form'),
    path('programs/<int:program_id>/', program_details, name='program_details'),
    path('programs/<int:program_id>/form/',
         program_edit_form, name='program_edit_form'),
]
