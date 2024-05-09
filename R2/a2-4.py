import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

@app.route("/", methods=["GET"])
# GETメソッドでのアクセスは以下が実行される．
def input():
    return render_template("a2-4in.html", title="イベント検索")


@app.route("/", methods=["POST"])
# POSTメソッドでのアクセスは以下が実行される．
def output():
    event_id = request.form["event_id"]
    # フォームからnameデータを取得する．
    try:
        id = int(event_id)
        name = events[id - 1].get("name")
        location = events[id - 1].get("location")
        if (id == 3): 
            date = '<font color="red">{}</font>'.format( events[id - 1].get("date"))
        else: 
            date = events[id - 1].get("date") 
    except ValueError:
        message = "整数値を入力してください"
        return render_template("a2-4out.html", message=message)
    except IndexError:
        message = "有効なidを入力してください"
        return render_template("a2-4out.html", message=message)
    return render_template("a2-4out.html", name=name, location=location, date=date, message="")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)