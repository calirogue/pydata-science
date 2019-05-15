-- 1. The general syntax of SELECT statments is:
select COLUMN1, COLUMN2, ... from TABLE1;

-- 2. To retrieve a list of all country names and their IDs from the 
-- table we would issue:
select ID, NAME from COUNTRY ;

-- 3. To retrieve all columns from the COUNTRY table we could use "*" instead of 
-- specifying individual column names:
select * from COUNTRY ;

-- 4. The WHERE clause can be added to your query to filter results or get specific 
-- rows of data. To retrieve data for all rows in the COUNTRY table where the ID 
-- is less than 5:
select * from COUNTRY where ID < 5 ;

-- 5. n case of character based columns the values of the predicates in the where 
-- clause need to be enclosed in single quotes. To retrieve the data for the 
-- country with country code "CA" we would issue:
select * from COUNTRY where CCODE = 'CA';

-- Vocab -- 

-- COUNT: 
-- COUNT() is a built in database function that retrieves the number of rows 
-- that match the query criteria. To get the total number of rows in a given table,
-- simply issue:
select COUNT(*) from tablename


-- DISTINCT:
-- DISTINCT is used to remove duplicate values from a result set. To retrieve 
-- unique values in a column issue:
select DISTINCT columnname from tablename


-- In the MEDALS table mentioned above there may be a lot of rows where the 
-- COUNTRY value is CANADA. Let's say you want to retrieve the list of unique 
-- countries that received GOLD medals, that is, removing all duplicate values 
-- of the same country. To do so, issue a query like:
select DISTINCT COUNTRY from MEDALS where MEDALTYPE = 'GOLD'

-- LIMIT: 
-- LIMIT is used for restricting the number of rows retrieved from the database. 
-- To retrieve just the first 10 rows in a table:
select * from tablename LIMIT 10

-- This can be very useful to examine the result set by looking at just a few 
-- rows instead of retrieving the entire result set which may be very large. 
-- For example to retrieve just a few rows in the MEDALS table for a particular 
-- year, you can issue:
select * from MEDALS where YEAR = 2018 LIMIT 5