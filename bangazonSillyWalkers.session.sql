
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
  p.id ProgramId,
  p.title ProgramName,
  emp.first_name,
  emp.last_name
from hrapp_program p
  join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
  join hrapp_employee emp on tp.employee_id = emp.id 
