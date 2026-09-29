-- Тестовые пользователи
INSERT INTO users (email, password_hash, first_name, last_name, role) VALUES
    ('user@test.com',  'fake_hash_user',  'Иван',  'Иванов',  'user'),
    ('admin@test.com', 'fake_hash_admin', 'Админ', 'Главный', 'admin');

-- Балансы первого пользователя (id = 1)
INSERT INTO balances (user_id, currency, amount) VALUES
    (1, 'RUB', 100.00);
    