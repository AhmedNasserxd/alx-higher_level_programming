-- creates the table force_name
-- data: id INT, name VARCHAR(256) can’t be null
-- database name will be passed as an argument
-- script shouldn't fail if table exists

CREATE TABLE IF NOT EXISTS force_name (
       id INT,
       name VARCHAR(256) NOT NULL
);
