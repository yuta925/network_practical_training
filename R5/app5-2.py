import math
# 数学関数用モジュールのインポート
import sqlite3

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


def get_distance(latitude, longitude):
    # 緯度経度をもとに神戸三田キャンパス（緯度34.915408，経度135.163968）からの距離を計算する関数．
    distance = 6371 * math.acos(
        math.cos(math.radians(34.915408))
        * math.cos(math.radians(latitude))
        * math.cos(math.radians(longitude) - math.radians(135.163968))
        + math.sin(math.radians(34.915408)) * math.sin(math.radians(latitude))
    )
    return distance


@app.route("/", methods=["GET"])
def database():
    data_list = []
    # データリストの初期化．
    db = get_db()
    cur = db.execute("SELECT * FROM games")
    for item in cur.fetchall():
        distance = get_distance(latitude=item[4], longitude=item[5])
        # 緯度経度から距離を計算する．
        tuple = list(item)
        # データベースのタプルをリスト化する．
        tuple.append(distance)
        # タプルに距離データを追加する．
        data_list.append(tuple)
        # タプルをデータリストに加える．
    schema = ["ID", "対戦相手", "日付", "場所", "緯度", "経度", "距離"]
    return render_template(
        "sample5-1a.html",
        title="Pythonとデータベースの連携",
        schema=schema,
        table=data_list,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port=5001)