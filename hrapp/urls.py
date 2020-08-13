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
    path('computers/', computer_list, name='computer_list'),
    path('computers/<int:computer_id>/', computer_details, name='computer'),
    path('computer/form', computer_form, name='computer_form'),
    path('employees/<int:employee_id>/', employee_details, name='employee'),
    path('programs/', program_list, name='program_list'),
    path('programs/form', program_form, name='program_form'),
    path('past_programs/', past_program_list, name='past_program_list'),
    path('programs/<int:program_id>/', program_details, name='program_details'),
    path('programs/<int:program_id>/form/',
         program_edit_form, name='program_edit_form'),
]
