import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from hrapp.models import Program


def create_program(cursor, row):
    _row = sqlite3.Row(cursor, row)

    program = Program()
    program.id = _row['program_id']
    program.title = _row['title']
    program.start_date = _row['start_date']
    program.end_date = _row['end_date']
    program.capacity = _row['capacity']

    return program


def get_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_program
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select
                p.id program_id,
                p.title,
                p.end_date,
                p.capacity,
                p.start_date
            from hrapp_program p
            WHERE p.id = ?
        """, (program_id,))

        return db_cursor.fetchone()


def program_details(request, program_id):
    if request.method == 'GET':
        program = get_program(program_id)
        template_name = 'programs/detail.html'
        return render(request, template_name, {'program': program})

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
