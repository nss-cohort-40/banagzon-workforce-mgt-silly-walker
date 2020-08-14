import sqlite3
from django.shortcuts import render, redirect, reverse 
from hrapp.models import Employee
from ..connection import Connection


def employee_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                e.id,
                e.first_name,
                e.last_name,
                e.start_date,
                e.is_supervisor,
                e.department_id
            from hrapp_employee e
            """)

            all_employees = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                employee = Employee()
                employee.id = row['id']
                employee.first_name = row['first_name']
                employee.last_name = row['last_name']
                employee.start_date = row['start_date']
                employee.is_supervisor = row['is_supervisor']
                employee.department_id = row['department_id']

                all_employees.append(employee)

        template = 'employees/employee_list.html'
        context = {
            'employees': all_employees
        }

        return render(request, template, context)

    elif request.method == 'POST':
            form_data = request.POST
            is_supervisor = None
            if form_data['is_supervisor'] == 'on':
                is_supervisor = 1
            else: 
                is_supervisor = 0

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                INSERT INTO hrapp_employee
                (
                    first_name, last_name, start_date, department_id, is_supervisor
                )
                VALUES (?, ?, ?, ?, ? )
                """,
                (form_data['first_name'], form_data['last_name'], 
                form_data['start_date'], form_data['department_id'], 
                is_supervisor))
            

            return redirect(reverse('hrapp:employee_list'))