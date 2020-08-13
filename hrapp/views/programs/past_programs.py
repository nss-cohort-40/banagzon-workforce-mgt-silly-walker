import sqlite3
from django.shortcuts import render, redirect, reverse
from hrapp.models import Program
from ..connection import Connection
from datetime import date


def past_program_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.title,
                p.end_date,
                p.capacity,
                p.start_date,
                emp.first_name,
                emp.last_name
            from hrapp_program p
                join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
                join hrapp_employee emp on tp.employee_id = emp.id 
            WHERE p.start_date <= "2020-08-11"
            """)

            all_programs = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                program = Program()
                program.id = row['id']
                program.title = row['title']
                program.start_date = row['start_date']
                program.end_date = row['end_date']
                program.capacity = row['capacity']
                program.first_name = row['first_name']
                program.last_name = row['last_name']

                all_programs.append(program)

        template = 'programs/past_programs.html'
        context = {
            'programs': all_programs
        }

        return render(request, template, context)
