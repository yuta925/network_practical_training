import sqlite3
from datetime import datetime

from flask import Flask, g, render_template

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("sample.db")
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d'):
    return datetime.strptime(value, format)

@app.route("/", methods=["GET"])
def database():
    db = get_db()
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall()
    close_db()
    schema = ["ID", "日付", "イベント名", "場所"]
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template(
        "a5-2.html",
        schema=schema,
        table=table,
        current_date=current_date,
    )

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)
