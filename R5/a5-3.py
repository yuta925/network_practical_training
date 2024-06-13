import sqlite3
from datetime import datetime
from flask import Flask, g, render_template, request

app = Flask(__name__)

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("a5-1.db")
    return g.db

def close_db():
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/", methods=["GET"])
def input():
    return render_template("a5-3.html")

@app.route("/add", methods=["POST"])
def add_event():
    date = request.form['date']
    name = request.form['name']
    place = request.form['place']
    db = get_db()
    db.execute("INSERT INTO events (date, name, place) VALUES (?, ?, ?)", (date, name, place))
    db.commit()
    cur = db.execute("SELECT * FROM events")
    # SELECT文の実行．結果はcurに代入される．
    table = cur.fetchall()
    # 実行結果の取得．タプルのリストとして得られる．
    close_db()
    message = 'eventsテーブルに追加しました'
    return render_template(
        "a5-3.html",
        message=message
    )

@app.route("/events", methods=["GET"])
def show_events():
    db = get_db()
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall()
    close_db()
    schema = ["ID", "日付", "イベント名", "場所"]
    return render_template("events.html", table=table, schema=schema)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)
