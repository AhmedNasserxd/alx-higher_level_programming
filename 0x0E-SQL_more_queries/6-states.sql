-- creates the database hbtn_0d_usa and the table states
-- data: id INT unique, auto generated, can’t be null and is a primary key 
-- name VARCHAR(256), can't be null
-- shouldn't fail if either already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
);
