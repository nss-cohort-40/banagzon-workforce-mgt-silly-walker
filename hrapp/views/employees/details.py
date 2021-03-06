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
            e.start_date,
            e.department_id,
            e.is_supervisor,
            d.name department_name,
            c.make as computer_make,
            c.model as computer_model,
            p.title as program_title
            
        FROM hrapp_employee e
            LEFT JOIN hrapp_department d ON e.department_id = d.id
            LEFT JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
            LEFT JOIN hrapp_computer c ON ec.computer_id = c.id
            LEFT JOIN hrapp_employee_training_program etp ON e.id = etp.employee_id
            LEFT JOIN hrapp_program p ON etp.trainingprogram_id = p.id
            WHERE e.id = ?
        """, (employee_id,))

        dataset = db_cursor.fetchall()

        employee = Employee()
        employee.id = dataset[0]['employee_id']
        employee.first_name = dataset[0]['first_name']
        employee.last_name = dataset[0]['last_name']
        employee.start_date = dataset[0]['start_date']
        employee.department_id = dataset[0]['department_id']
        employee.is_supervisor = dataset[0]['is_supervisor']
        employee.department_name = dataset[0]['department_name']
        employee.computer_make = dataset[0]['computer_make']
        employee.computer_model = dataset[0]['computer_model']
        employee.programs = []
        for row in dataset:
            employee.programs.append(row['program_title'])

        return employee


def employee_details(request, employee_id):
    if request.method == 'GET':
        employee = get_employee(employee_id)

        template = 'employees/detail.html'
        context = {
            'employee': employee
        }
        return render(request, template, context)

    elif request.method =='POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_employee
                SET first_name = ?,
                    last_name = ?,
                    start_date = ?, 
                    department_id = ?,
                    is_supervisor = ?
                Where id = ?
                """,
                (form_data['first_name'], form_data['last_name'], 
                form_data['start_date'], form_data['department_id'], 
                form_data['is_supervisor'], employee_id))

                print(form_data['is_supervisor'])

            return redirect(reverse('hrapp:employee_list'))