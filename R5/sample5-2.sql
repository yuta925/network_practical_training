.open sample.db
.mode box
DROP TABLE IF EXISTS games;
CREATE TABLE games(id INTEGER PRIMARY KEY AUTOINCREMENT, opponent TEXT, date TEXT, place TEXT, latitude REAL, longitude REAL);
INSERT INTO games(opponent, date, place, latitude, longitude) VALUES('ドイツ','2022-11-23','ドーハ', 25.263611, 51.448056);
INSERT INTO games(opponent, date, place, latitude, longitude) VALUES('コロンビア','2023-03-28','大阪', 34.615383, 135.516656);
INSERT INTO games(opponent, date, place, latitude, longitude) VALUES('ブラジル','2026-06-12','ニューヨーク', 40.813611,-74.074444);
SELECT * FROM games WHERE date > CURRENT_DATE;