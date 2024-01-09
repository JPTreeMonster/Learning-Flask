-- Database table
DROP TABLE IF EXISTS InquireTable;
CREATE TABLE IF NOT EXISTS 'InquireTable' (
    'ID'    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name'  TEXT NOT NULL,
    'email' TEXT NOT NULL,
    'inquiry'   TEXT NOT NULL
);

INSERT INTO 'InquireTable'('name','email','inquiry') VALUES ('Jo Bloggs','Example@email.com', 'Hi my name is Jo :)');