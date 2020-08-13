import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Program


def get_program_employees(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_program
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            p.id program_id,
            p.title,
            p.end_date,
            p.capacity,
            p.start_date,
            emp.first_name,
            emp.last_name
        from hrapp_program p
            join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
            join hrapp_employee emp on tp.employee_id = emp.id;
        """, (program_id,))

        return db_cursor.fetchone()


def program_details(request, program_id):
    if request.method == 'GET':
        program = get_program_employees(program_id)
        template_name = 'programs/detail.html'
        return render(request, template_name, {'program': program})
