import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Program, Employee
from ..connection import Connection
from datetime import date


def create_past_program(cursor, row):
    _row = sqlite3.Row(cursor, row)

    program = Program()
    program.id = _row["id"]
    program.title = _row["title"]
    program.start_date = _row["start_date"]
    program.end_date = _row["end_date"]
    program.capacity = _row["capacity"]
    program.employees = []

    employee = Employee()
    employee.id = _row["EmployeeId"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]

    return (program, employee,)


def past_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_past_program
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.title,
                p.end_date,
                p.capacity,
                p.start_date,
                emp.id EmployeeId,
                emp.first_name,
                emp.last_name
            from hrapp_program p
                LEFT join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
                LEFT join hrapp_employee emp on tp.employee_id = emp.id 
            WHERE p.start_date <= "2020-08-11"
            """)

            dataset = db_cursor.fetchall()

        program_groups = {}

        for (program, employee) in dataset:

            if program.id not in program_groups:
                program_groups[program.id] = program
                if (employee.id is not None):
                    program_groups[program.id].employees.append(employee)

            else:
                program_groups[program.id].employees.append(employee)

        template = 'programs/past_programs.html'
        context = {
            'programs': program_groups.values()
        }

        return render(request, template, context)
