CREATE DATABASE mydatabase;
\c mydatabase;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL
);
INSERT INTO users (name, email) VALUES ('Musa Ibrahim', 'musaaj@example.com');
SELECT * FROM users;
UPDATE users SET email = 'newemail@example.com' WHERE name = 'Musa Ibrahim';
SELECT * FROM users WHERE name = 'Musa Ibrahim';
DELETE FROM users WHERE name = 'Musa Ibrahim';
SELECT * FROM users;
