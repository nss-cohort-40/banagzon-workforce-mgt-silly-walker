
 select d.id,
      d.name,
      d.budget, 
      COUNT(e.id) as employee_count
  from hrapp_department d  
      LEFT JOIN hrapp_employee e ON d.id = e.department_id
  GROUP BY d.name;

DROP TABLE hrapp_employeecomputer;

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p;

select 
  d.id,
  d.name,
  d.budget, 
  e.first_name,
  e.last_name, 
  e.department_id

from hrapp_employee e  
JOIN hrapp_department d ON e.department_id = d.id
GROUP BY e.last_name;