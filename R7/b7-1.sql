.open b7-1.db
.mode box
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title VARCHAR(100),
    author VARCHAR(100),
    genre VARCHAR(50),
    published_year INT
);

INSERT INTO books (title, author, genre, published_year) VALUES ('吾輩は猫である', '夏目漱石', '小説', 1905);
INSERT INTO books (title, author, genre, published_year) VALUES ('こころ', '夏目漱石', '小説', 1914);
INSERT INTO books (title, author, genre, published_year) VALUES ('走れメロス', '太宰治', '短編小説', 1940);
INSERT INTO books (title, author, genre, published_year) VALUES ('人間失格', '太宰治', '小説', 1948);
INSERT INTO books (title, author, genre, published_year) VALUES ('雪国', '川端康成', '小説', 1947);
INSERT INTO books (title, author, genre, published_year) VALUES ('千羽鶴', '川端康成', '小説', 1952);
INSERT INTO books (title, author, genre, published_year) VALUES ('ノルウェイの森', '村上春樹', '小説', 1987);
INSERT INTO books (title, author, genre, published_year) VALUES ('1Q84', '村上春樹', '小説', 2009);
INSERT INTO books (title, author, genre, published_year) VALUES ('火花', '又吉直樹', '小説', 2015);
INSERT INTO books (title, author, genre, published_year) VALUES ('君の名は。', '新海誠', '小説', 2016);

