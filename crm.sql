------------------------------------------
--DDL statement for table 'Dispensary' database--
--------------------------------------------

CREATE TABLE DISPENSARYTABLE (
                            DISPENSARY VARCHAR(30) NOT NULL, 
                            INTAKE_MANAGER VARCHAR(15) NOT NULL,
                            PHONE VARCHAR(15) NOT NULL,
                            DISPENSARY_ADDRESS VARCHAR(35) NOT NULL,
                            FOLLOW_UP_DATE VARCHAR(20) NOT NULL,
                            INTAKE_EMAIL VARCHAR(20) NOT NULL,
                            NOTES VARCHAR(200),
                            DISPENSARY_EMAIL VARCHAR(20));
                            
     
SELECT NAME FROM DISPENSARYTABLE;

SELECT NOTES FROM DISPENSARYTABLE;

select NOTES FROM DISPENSARYTABLE WHERE NOTES LIKE 'W%';
