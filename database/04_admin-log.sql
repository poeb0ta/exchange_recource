CREATE TABLE admin_log(
    id serial primary key,
    admin_id integer references users(id),
    transaction_id integer references transactions(id)  on delete cascade,
    admin_action varchar(20) not null,
    check (admin_action in ('approve', 'reject', 'modify')),
    admin_comment text,
    created_at timestamp not null default now()
);