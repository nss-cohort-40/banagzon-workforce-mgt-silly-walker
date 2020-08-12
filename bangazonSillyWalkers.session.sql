SELECT
    d.name,
    d.budget, 
    d.id department_id, 
    e.first_name,
    e.last_name
FROM hrapp_department d
JOIN hrapp_employee e on d.id = e.department_id


select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p
