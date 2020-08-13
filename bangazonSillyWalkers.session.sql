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


select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date
from hrapp_program p;

SELECT
  c.id,
  c.make,
  c.model,
  c.purchase_date,
  c.decommission_date,
  ec.employee_id emp_id
FROM hrapp_computer c
  LEFT JOIN hrapp_employeecomputer ec ON c.id = ec.computer_id
WHERE c .id = 4;

INSERT INTO hrapp_employeecomputer
VALUES
  (null, 2, 1, "2020-08-11", "None");

DELETE FROM hrapp_employeecomputer
WHERE id = 4;

SELECT
  p.id ProgramId,
  p.title ProgramName,
  emp.first_name,
  emp.last_name
from hrapp_program p
  join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
  join hrapp_employee emp on tp.employee_id = emp.id

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


SELECT
  e.id as employee_id,
  e.first_name,
  e.last_name,
  e.department_id,
  d.name department_name,
  c.make as computer_make,
  c.model as computer_model,
  p.title as program_title
FROM hrapp_employee e
  LEFT JOIN hrapp_department d ON e.department_id = d.id
  LEFT JOIN hrapp_employeecomputer ec ON e.id = ec.employee_id
  LEFT JOIN hrapp_computer c ON ec.computer_id = c.id
  LEFT JOIN hrapp_employee_training_program etp ON e.id = etp.employee_id
  LEFT JOIN hrapp_program p ON etp.trainingprogram_id = p.id
  WHERE e.id = 1;


INSERT INTO hrapp_employee
VALUES (NULL, "Bob", "Joe", 2020-05-06, 0, 2);