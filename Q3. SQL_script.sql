-- Question No. 3: 
-- Write SQL Query to create a database named datum labs.
-- In the database, create a table named employee with columns emp_id, emp_name, emp_age, emp_exp, dep_id, and 
-- create a second table named department with columns dep_id, dep_name. 
-- Insert 10 records into the employee table and 
-- 5 into the department table. 
-- After inserting records into tables, group by dep_id and show how many employees are in each department.



-- CREATE  DATABASE datum_labs;
CREATE TABLE employee(
    emp_id INT,
    emp_name VARCHAR(100),
    emp_age INT,
    emp_exp INT,
    dep_id INT
);
CREATE TABLE department(
    dep_id INT,
    dep_name VARCHAR(100)
);
INSERT INTO employee
VALUES 
(001, "A", 23, 1, 001), 
(002, "B", 24, 2, 002),
(003, "C", 25, 3, 003),
(004, "D", 26, 4, 004),
(005, "E", 27, 5, 005),
(006, "F", 28, 6, 005),
(007, "G", 29, 7, 004),
(008, "H", 30, 8, 003),
(009, "I", 31, 9, 002),
(010, "J", 32, 10, 001);

INSERT INTO department
VALUES
(001, "Comp Sci"),
(002, "Software Engr"),
(003, "IT"),
(004, "Comp Engr"),
(005, "Data Science")
;

SELECT dep_id,
       (SELECT COUNT(*)
        FROM employee e
        WHERE e.dep_id = d.dep_id) AS num_employees
FROM department d;
