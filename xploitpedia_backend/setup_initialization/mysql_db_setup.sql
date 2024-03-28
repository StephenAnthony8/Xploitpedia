-- prepares a MySQL server for the project
-- db/user names & db names are solely for presentation

CREATE DATABASE IF NOT EXISTS xploitpedia;
CREATE USER IF NOT EXISTS 'x_user'@'localhost' IDENTIFIED BY 'x_user_pwd';
GRANT ALL PRIVILEGES ON `xploitpedia`.* TO 'x_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'x_user'@'localhost';
FLUSH PRIVILEGES;
