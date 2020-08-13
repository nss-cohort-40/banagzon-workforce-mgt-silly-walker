DELETE 
FROM hrapp_computer;

DELETE 
FROM hrapp_employeecomputer;

select
  c.id,
  c.make,
  c.model,
  c.purchase_date,
  c.decommission_date
from hrapp_computer c;

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p
