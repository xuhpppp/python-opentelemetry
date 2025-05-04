CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL,
    total_amount INTEGER NOT NULL
);

INSERT INTO orders (id, customer_id, order_date, total_amount) VALUES
    (1, 1001, '2025-05-01 10:30:00', 250),
    (2, 1002, '2025-05-03 14:15:00', 400)
ON CONFLICT (id) DO NOTHING;