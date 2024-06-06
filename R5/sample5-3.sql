.open sample.db
.mode box
DROP TABLE IF EXISTS person;
CREATE TABLE person(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);
INSERT INTO person(name) VALUES('財津一郎');
INSERT INTO person(name) VALUES('田宮二郎');
SELECT * FROM person;