
-- SQL to create the join table for Employee Training Programs [start]
;
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


