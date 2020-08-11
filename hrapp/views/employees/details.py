import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hrapp.models import Employee, Department
from ..connection import Connection


def get_employee(employee_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id as employee_id,
            e.first_name,
            e.last_name,
            e.department_id,
            d.name department_name
        FROM hrapp_employee e
        JOIN hrapp_department d ON e.department_id = d.id        WHERE e.id = ?
        """, (employee_id,))

        return db_cursor.fetchone()


@login_required
def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/detail.html'
        context = {
            'employee': employee
        }

        return render(request, template, context)
