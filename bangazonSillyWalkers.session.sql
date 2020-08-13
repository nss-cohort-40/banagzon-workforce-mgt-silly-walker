
SELECT
  e.id as employee_id,
  e.first_name,
  e.last_name,
  e.department_id,
  d.name department_name,
  c.make as computer_make
FROM hrapp_employee e
  JOIN hrapp_department d ON e.department_id = d.id
  JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
  JOIN hrapp_computer c ON ec.computer_id = c.id;

DROP TABLE hrapp_employeecomputer;

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p
WHERE p.start_date >= "2020-08-11";

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p
from hrapp_program p;
