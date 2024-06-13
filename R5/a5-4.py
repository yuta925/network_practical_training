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
def show_events():
    db = get_db()
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall()
    close_db()
    schema = ["ID", "日付", "イベント名", "場所"]
    return render_template("a5-4.html", table=table, schema=schema)

@app.route("/delete", methods=["POST"])
def add_event():
    id = request.form['id']
    db = get_db()
    db.execute("DELETE FROM events WHERE id = ?", (id))   
    cur = db.execute("SELECT * FROM events")
    table = cur.fetchall() 
    db.commit()
    close_db()
    message = '削除しました'
    schema = ["ID", "日付", "イベント名", "場所"]
    return render_template(
        "a5-4.html",
        message=message,table=table, schema=schema
    )

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)
