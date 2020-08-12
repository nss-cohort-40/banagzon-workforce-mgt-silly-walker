DELETE 
FROM hrapp_computer;

select
    c.id,
    c.make,
    c.model,
    c.purchase_date,
    c.decommission_date
from hrapp_computer c