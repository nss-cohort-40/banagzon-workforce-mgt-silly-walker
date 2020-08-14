import sqlite3
from django.shortcuts import render
from ..connection import Connection
from .details import get_employee


def employee_form(request):  
    if request.method == 'GET':
        template = 'employees/employees_form.html'

    return render(request, template, context=None)

def employee_edit_form(request, employee_id):

    if request.method == 'GET':
        employee = get_employee(employee_id)
        print(employee.is_supervisor)
        template = 'employees/employees_form.html'
        context = {
            'employee' : employee
        }
    
    return render(request, template, context)
