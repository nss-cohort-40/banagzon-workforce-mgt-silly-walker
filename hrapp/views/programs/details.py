import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Program, Employee


def create_program(cursor, row):
    _row = sqlite3.Row(cursor, row)

    program = Program()
    program.id = _row['id']
    program.title = _row['title']
    program.start_date = _row['start_date']
    program.end_date = _row['end_date']
    program.capacity = _row['capacity']

    employee = Employee()
    employee.id = _row["EmployeeId"]
    employee.first_name = _row["first_name"]
    employee.last_name = _row["last_name"]
    program.employee = employee

    return program


def get_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_program
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
        WHERE p.id = ?
        """, (program_id,))

        return db_cursor.fetchall()


def program_details(request, program_id):
    if request.method == 'GET':
        current_program = {}

        program = get_program(program_id)
        current_program["id"] = program[0].id
        current_program["title"] = program[0].title
        current_program["start_date"] = program[0].start_date
        current_program["end_date"] = program[0].end_date
        current_program["capacity"] = program[0].capacity
        current_program["employees"] = []
        for program in program:
            current_program["employees"].append(program.employee)

        template_name = 'programs/detail.html'

        return render(request, template_name, {'program': current_program})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a program
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE hrapp_program
                SET title = ?,
                    end_date = ?,
                    capacity = ?,
                    start_date = ?
                WHERE id = ?
                """,
                                  (
                                      form_data['title'], form_data['end_date'],
                                      form_data['capacity'], form_data['start_date'], program_id,
                                  ))

            return redirect(reverse('hrapp:program_list'))

        # Check if this POST is for deleting a program
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM hrapp_program
                    WHERE id = ?
                """, (program_id,))

            return redirect(reverse('hrapp:program_list'))
