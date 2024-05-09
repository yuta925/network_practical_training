from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def input():
    return render_template("b2-2.html")

@app.route("/", methods=["POST"])
def output():
    try:
        name = request.form.get("event_name")
        if not name:
            raise ValueError("イベント名が入力されていません")
        date_str = request.form.get("event_date")
        if not date_str:
            raise ValueError("日付が入力されていません")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        dt = datetime.now()
        period = date - dt
        if period.days < 0:
            raise ValueError("指定された日付は過去の日付です")
        message = "{}[{}]まであと{}日です．".format(name, date_str, period.days+1)
    except ValueError as e:
        message = str(e)
    except (TypeError, IndexError):
        message = "正しく入力してください．"
    return render_template("b2-2.html", message=message)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)