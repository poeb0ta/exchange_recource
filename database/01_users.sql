CREATE TABLE users(
    id serial primary key,
    email varchar(120) unique not null,
    password_hash varchar(255) not null,
    first_name varchar(15) not null,
    last_name varchar(20) not null,
    role varchar(20) not null default 'user'
    check(role in ('user', 'admin')),
    is_active boolean not null default true
);
ALTER TABLE users
ADD COLUMN bank_requisites varchar(255);