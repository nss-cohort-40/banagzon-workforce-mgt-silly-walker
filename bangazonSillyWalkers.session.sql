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


INSERT INTO hrapp_employee_training_program
  (employee_id, trainingprogram_id)
VALUES
  (2, 1);
INSERT INTO hrapp_employee_training_program
  (employee_id, trainingprogram_id)
VALUES
  (3, 1);


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
  LEFT join hrapp_employee_training_program tp on tp.trainingprogram_id = p.id
  LEFT join hrapp_employee emp on tp.employee_id = emp.id
WHERE p.start_date <= "2020-08-11";

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
