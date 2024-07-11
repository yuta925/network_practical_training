import sqlite3
from flask import Flask, g, render_template
from geopy.distance import geodesic

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

KOBE_SANDA_COORDS = (34.915408, 135.163968)

@app.route('/', methods=['GET'])
def datebase():
    db = get_db()
    cur = db.execute('''
    SELECT e.name AS event_name, e.date, p.city_name AS place, p.country_name, p.latitude, p.longitude
    FROM events e
    JOIN places p ON e.place = p.city_name
    ''')
    events = cur.fetchall()
    close_db()

    event_distances = []
    for event in events:
        event_coords = (event[4], event[5])
        distance = geodesic(KOBE_SANDA_COORDS, event_coords).kilometers
        event_distances.append((event[0], event[1], event[2], event[3], distance))

    event_distances.sort(key=lambda x: x[4])

    tables = event_distances
    return render_template('b6-2.html', tables=tables)

if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost")
