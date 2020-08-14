from .employees.employee_list import employee_list
from .home import home
from .auth.logout import logout_user
from .departments.department_list import department_list
from .departments.department_details import department_details, get_department
from .computers.list import computer_list
from .computers.details import computer_details
from .computers.form import computer_form
from .employees.details import employee_details
from .programs.program_list import program_list
from .programs.form import program_edit_form, program_form
from .programs.details import program_details
from .programs.past_programs import past_program_list
from .employees.employees_form import employee_form

from .programs.past_program_details import get_program_employees
from .auth.login import login
