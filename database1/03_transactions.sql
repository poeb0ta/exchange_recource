CREATE TABLE transactions(
    id serial primary key,
    user_id integer not null references users(id) on delete cascade,
    from_currency varchar(3) not null,
    to_currency varchar(3) not null,
    amount_sent numeric(18,3) not null,
    amount_get numeric(18,3),
    rate numeric(18,6),
    status_transaction varchar(20) not null default 'pending'
    check(status_transaction in ('pending', 'approved','rejected', 'modified')),
    admin_comment text,
    created_at timestamp not null default now(),
    updated_at timestamp not null default now()
);