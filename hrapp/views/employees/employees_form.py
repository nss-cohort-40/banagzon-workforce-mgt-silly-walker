import sqlite3
from django.shortcuts import render
from ..connection import Connection

def employee_form(request):  
    if request.method == 'GET':
        template = 'employees/employees_form.html'

        return render(request, template, context=None)

def employee_edit_form(request, employee_id):
    if request.method == 'GET':
        template = 'employees/employees_form.html'