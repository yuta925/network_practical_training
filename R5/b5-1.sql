-- b5-1.sql

.open a5-1.db

-- Create the places table
DROP TABLE IF EXISTS places;
CREATE TABLE places(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT,
    country_name TEXT,
    latitude REAL,
    longitude REAL
);

-- Insert the places
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('カシマ', '日本', 35.973418, 140.640604);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('富山', '日本', 36.69529, 137.21134);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('ノエスタ', '日本', 34.646666, 135.179722);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('埼玉', '日本', 35.861729, 139.645482);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('国立', '日本', 35.675064, 139.710236);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('パナスタ', '日本', 34.800022, 135.470543);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('Eピース', '日本', 34.385203, 132.455292);
INSERT INTO places(city_name, country_name, latitude, longitude) VALUES('札幌ド', '日本', 43.000084, 141.409606);

SELECT * FROM places;

-- e) Join events and places to display all event names, dates, places, and country names
SELECT e.name AS event_name, e.date, p.city_name AS place, p.country_name
FROM events e
JOIN places p ON e.place = p.city_name;

-- f) Sort events in Japan by date
SELECT e.name AS event_name, e.date, p.city_name AS place, p.country_name
FROM events e
JOIN places p ON e.place = p.city_name
WHERE p.country_name = '日本'
ORDER BY e.date;

-- g) Count the number of events in Japan
SELECT COUNT(*) AS event_count
FROM events e
JOIN places p ON e.place = p.city_name
WHERE p.country_name = '日本';

-- Query to fetch all events with their respective places and countries
SELECT e.name AS event_name, e.date, p.city_name AS place, p.country_name, p.latitude, p.longitude
FROM events e
JOIN places p ON e.place = p.city_name;
