-- Database table
DROP TABLE IF EXISTS LoginDetailsTable;
CREATE TABLE IF NOT EXISTS 'LoginDetailsTable' (
    'ID'    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'username'  TEXT NOT NULL,
    'password' TEXT NOT NULL
);

INSERT INTO 'LoginDetailsTable'('username','password') VALUES ('JP McC','password');