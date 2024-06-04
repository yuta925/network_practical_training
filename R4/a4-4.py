from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def fileupload():
    return render_template("a4-4.html")


@app.route("/", methods=["POST"])
def filewrite():
    message = ""
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    try:
        datetime.strptime(event_date, "%Y-%m-%d")
        with open("a4-3.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{event_date},{event_name}")
        message = "書き込み終了"
    except ValueError:
        message = "日付が無効です。YYYY-MM-DD形式で入力してください。"
    return render_template("a4-4.html", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")