SELECT
    d.name,
    d.budget,  
    e.first_name,
    e.last_name,
    e.department_id 
FROM hrapp_department d
JOIN hrapp_employee e on d.id = e.department_id;

SELECT COUNT(department_id) as dept_count
FROM hrapp_employee
where department_id = 2;

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p
