CREATE TABLE balances(
    id serial primary key,
    user_id integer not null references users(id) on delete cascade,
    currency varchar(3) not null,
    amount numeric(18,3) not null default 0,
    created_at timestamp not null default now(),
    updated_at timestamp not null default now(),
    unique(user_id, currency)
);