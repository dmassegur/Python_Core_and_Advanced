create database mydb
use mydb
create table employeeDB(id int, name varchar(100), salary int)

## insert some data into dB
insert into employeeDB values(1,'david',10000)
insert into employeeDB values(2,'marija',20000)

## display all the data
select * from employeeDB
