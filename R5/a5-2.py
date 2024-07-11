import sqlite3
from datetime import datetime

from flask import Flask, g, render_template

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
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
    table1 = cur.fetchall()
    cur = db.execute("SELECT * FROM events WHERE name LIKE '鹿島%'")
    table2 = cur.fetchall()
    cur = db.execute("SELECT * FROM events WHERE date >= date('now')")
    table3 = cur.fetchall()
    cur = db.execute("SELECT * FROM events WHERE id%2=0 and place='ノエスタ'")
    table4 = cur.fetchall()
    close_db()
    schema = ["ID", "日付", "イベント名", "場所"]
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template(
        "a5-2.html",
        schema=schema,
        table1=table1,
        table2=table2,
        table3=table3,
        table4=table4,
        current_date=current_date,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
