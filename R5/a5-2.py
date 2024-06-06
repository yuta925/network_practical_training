import sqlite3
from datetime import datetime

# sqlite用モジュールのインポート
from flask import Flask, g, render_template

# グローバル変数gのインポート


app = Flask(__name__)


def get_db():
    if "db" not in g:
        # gはリクエストごとに用意されるFlaskのオブジェクト
        # gに"db"が含まれていない場合にデータベースへの接続が行われる．
        g.db = sqlite3.connect("sample.db")
        # データベースへの接続
    return g.db


def close_db():
    db = g.pop("db", None)
    # gから"db"を取り出す．
    if db is not None:
        # gに"db"が含まれていた場合にはデータベースとの接続を終了する．
        db.close()
        # データベースの接続終了

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d'):
    return datetime.strptime(value, format)

@app.route("/", methods=["GET"])
def database():
    db = get_db()
    db.commit()
    # データベースの変更点を書き込む．
    cur = db.execute("SELECT * FROM events")
    # SELECT文の実行．結果はcurに代入される．
    table = cur.fetchall()
    # 実行結果の取得．タプルのリストとして得られる．
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