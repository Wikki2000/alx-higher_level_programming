-- Creates the database hbtn_0d_usa and the table cities on MYSQL server
CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;

-- Use created database
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY(id) REFERENCES state(id)
	);
