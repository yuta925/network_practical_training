.open b7-1.db
.mode box
DROP TABLE IF EXISTS events;
CREATE TABLE events(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    date TEXT, 
    name TEXT, 
    place TEXT
);
INSERT INTO events(date, name, place) VALUES('2024-05-19','鹿島vs神戸','カシマ');
INSERT INTO events(date, name, place) VALUES('2024-05-22','今治vs神戸','富山');
INSERT INTO events(date, name, place) VALUES('2024-05-26','神戸vs東京V','ノエスタ');
INSERT INTO events(date, name, place) VALUES('2024-06-01','浦和vs神戸','埼玉');
INSERT INTO events(date, name, place) VALUES('2024-06-16','神戸vs川崎F','ノエスタ');
INSERT INTO events(date, name, place) VALUES('2024-06-22','G大阪vs神戸','国立');
INSERT INTO events(date, name, place) VALUES('2024-06-26','神戸vs町田','パナスタ');
INSERT INTO events(date, name, place) VALUES('2024-06-30','神戸vs鹿島','ノエスタ');
INSERT INTO events(date, name, place) VALUES('2024-07-05','広島vs神戸','Eピース');
INSERT INTO events(date, name, place) VALUES('2024-07-13','札幌vs神戸','札幌ド');
