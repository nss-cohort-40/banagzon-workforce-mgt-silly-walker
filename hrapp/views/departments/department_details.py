import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection

def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select 
            d.name,
            d.budget, 
            e.first_name,
            e.last_name, 
            e.department_id
        FROM hrapp_department d 
        LEFT JOIN hrapp_employee e ON e.department_id = ?
                """, (department_id,))

        return db_cursor.fetchone()

def department_details(request, department_id):
    if request.method == 'GET':
        department = get_department(department_id)
        
        template = 'departments/departments_detail.html'
        context = {
            'department': department,
        }

        return render(request, template, context)

    