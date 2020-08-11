SELECT
    e.id,
    e.first_name,
    e.last_name,
    e.department_id
FROM hrapp_employee e
    JOIN hrapp_department d ON e.department_id = d.id