-- Creates the database hbtn_0d_usa and the table states on your MySQL server.

-- Create Database
CREATE DATABASE
IF NOT EXISTS hbtn_0d_usa;

-- Use table
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
	);
