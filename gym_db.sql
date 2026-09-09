
create database gym_db;
use gym_db;
create table member(
id int  auto_increment primary key,
name varchar(100),
place varchar(100),
mobile varchar(15) unique,
plan enum("1 month","2 months","3 months","4 months","5 months","6 months"),
fee int,
joined_on date
);

select* from member;
show tables;

select * from member;