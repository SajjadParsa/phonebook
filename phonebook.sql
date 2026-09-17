create database if not exists phonebook;
use phonebook;
create table if not exists contacts(
    id int auto_increment primary key,
    name varchar(100) not null,
    phone varchar(20) not null,
    adress varchar(100),
    gmail varchar(100)
);
