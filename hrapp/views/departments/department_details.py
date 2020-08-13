import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from ..connection import Connection

def get_count(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT COUNT(department_id) as dept_count
        FROM hrapp_employee 
        WHERE department_id = ?
        """, (department_id))
        


def get_department(department_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.name,
            d.budget, 
            d.id as dept_id, 
            e.first_name,
            e.last_name
        FROM hrapp_department d
        JOIN hrapp_employee e on d.id = e.department_id 
        WHERE d.id = ?
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

    