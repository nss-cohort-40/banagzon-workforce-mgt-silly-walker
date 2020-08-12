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