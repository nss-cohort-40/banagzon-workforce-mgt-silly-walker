
-- SQL to create the join table for Employee Training Programs [start]
;
CREATE TABLE "hrapp_employee_training_program"
(
  "id" INTEGER NOT NULL PRIMARY KEY,
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


  CREATE TABLE "hrapp_employee_training_program"
  (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "employee_id" INTEGER NOT NULL,
    "trainingprogram_id" INTEGER NOT NULL,
    FOREIGN KEY ("employee_id") REFERENCES "hrapp_employee"
("Id"),
    FOREIGN KEY
("trainingprogram_id") REFERENCES "hrapp_program"
("Id")
  );
  -- [END of table creation]
  -- ;

  -- SQL to create some seed data for assinging training programs and employees
  ;
  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (1, 1);

  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (2, 2);

  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (3, 3);

  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (1, 2);

  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (2, 2);

  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (2, 1);
  INSERT INTO hrapp_employee_training_program
    (employee_id, trainingprogram_id)
  VALUES
    (3, 1);
  -- [END of Seed Data creation]
  -- ;


  <<<<<<< HEAD
=======
  select
    p.id,
    p.title,
    p.end_date,
    p.capacity,
    p.start_date,
    emp.id EmployeeId,
    emp.first_name,
    emp.last_name
  from hrapp_program p
    join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
    join hrapp_employee emp on tp.employee_id = emp.id
  WHERE p.start_date <= "2020-08-11";

  select
    d.id,
    d.name,
    d.budget,
    e.first_name,
    e.last_name,
    e.department_id
  FROM hrapp_employee e
    JOIN hrapp_department ON e.department_id = d.id
  GROUP BY e.last_name;


  select
    d.name,
    d.budget,
    e.first_name,
    e.last_name,
    e.department_id
  FROM hrapp_department d
    LEFT JOIN hrapp_employee e ON  e.department_id = d.id;


  INSERT INTO hrapp_employee
  VALUES
    (NULL, "Bob", "Joe", 2020-05-06, 0, 2);

  SELECT
    c.id,
    c.make,
    c.model,
    c.purchase_date,
    c.decommission_date,
    ec.employee_id emp_id
  FROM hrapp_computer c
    LEFT JOIN hrapp_employeecomputer ec on c.id = ec.computer_id;

  SELECT
    u.is_superuser
  FROM auth_user u;
  >>>>>>> master
