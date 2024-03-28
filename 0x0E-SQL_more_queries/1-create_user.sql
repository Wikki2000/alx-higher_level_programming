--- Ccreates the MySQL server user user_0d_1 with password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'

-- Grant all privileges to user_0d_1 on your MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost'
