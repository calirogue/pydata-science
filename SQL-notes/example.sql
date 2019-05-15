CREATE TABLE OINSTRUCTOR
  (ins_id INTEGER PRIMARY KEY NOT NULL, 
   lastname VARCHAR(15) NOT NULL, 
   firstname VARCHAR(15) NOT NULL, 
   city VARCHAR(15), 
   country CHAR(2)
  );
  
  
  
 INSERT INTO OINSTRUCTOR
  (ins_id, lastname, firstname, city, country)
  VALUES 
  (1, 'Ahuja', 'Rav', 'Toronto', 'CA')
;

INSERT INTO OINSTRUCTOR
  VALUES
  (2, 'Chong', 'Raul', 'Toronto', 'CA'),
  (3, 'Vasudevan', 'Hima', 'Chicago', 'US')
;

SELECT * FROM OINSTRUCTOR
;

SELECT firstname, lastname, country from OINSTRUCTOR where city='Toronto'
;

DELETE FROM OINSTRUCTOR where ins_id=2; 

SELECT * FROM INSTRUCTOR 
;
