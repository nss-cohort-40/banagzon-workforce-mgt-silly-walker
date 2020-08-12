SELECT
    d.name,
    d.budget, 
    d.id department_id, 
    e.first_name,
    e.last_name
FROM hrapp_department d
JOIN hrapp_employee e on d.id = e.department_id
