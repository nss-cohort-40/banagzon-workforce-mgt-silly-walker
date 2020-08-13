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

CREATE TABLE "hrapp_employee_training_program" (
	"id" INTEGER NOT NULL PRIMARY KEY,
  "employee_id" INTEGER NOT NULL,
  "trainingprogram_id" INTEGER NOT NULL,
    FOREIGN KEY (`employee_id`) REFERENCES "hrapp_employee"
(`Id`),
    FOREIGN KEY
(`trainingprogram_id`) REFERENCES "hrapp_program"
(`Id`)
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
  p.id,
  p.title,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date,
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
  join hrapp_employee emp on tp.employee_id = emp.id;

select
  p.id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date,
  emp.first_name,
  emp.last_name
from hrapp_program p
  join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
  join hrapp_employee emp on tp.employee_id = emp.id;

select
  p.id program_id,
  p.title,
  p.end_date,
  p.capacity,
  p.start_date,
  emp.first_name,
  emp.last_name
from hrapp_program p
  join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
  join hrapp_employee emp on tp.employee_id = emp.id;

