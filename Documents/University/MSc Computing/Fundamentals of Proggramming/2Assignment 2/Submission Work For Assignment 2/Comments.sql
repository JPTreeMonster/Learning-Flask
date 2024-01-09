DROP TABLE IF EXISTS CommentTable;
CREATE TABLE IF NOT EXISTS 'CommentTable' (
    'ID'    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name'  TEXT NOT NULL,
    'comment' TEXT NOT NULL
);

INSERT INTO 'CommentTable'('name','comment') VALUES ('Jo Bloggs', 'Hi my name is Jo :)');