CREATE TABLE history (
    id serial primary key,
    user_id integer references users(id) on delete set null,
    table_name varchar(20) not null,
    doing varchar(20) not null check(doing in ('insert','update','delete')),
    old_data JSONB,
    new_data JSONB,
    created_at timestamp not null default now()
);