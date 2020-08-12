import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Program
from ..connection import Connection
from .program_list import program_list


def get_program(program_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            p.id,
            p.title,
            p.end_date,
            p.capacity,
            p.start_date
        from hrapp_program p
        WHERE p.id = ?
        """, (program_id,))

        return db_cursor.fetchone()


def program_form(request):
    if request.method == 'GET':
        template = 'programs/form.html'

    return render(request, template, context=None)


def program_edit_form(request, program_id):

    if request.method == 'GET':
        program = get_program(program_id)

        template = 'programs/form.html'
        context = {
            'program': program,
        }

    return render(request, template, context)
