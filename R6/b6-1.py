from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = "イベントページ"
    if request.method == "POST":
        event_id = request.form["event_id"]
        events = {
            "1": {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024-4-4"},
            "2":{"name": "誕生日会", "location": "友達の家", "date": "2024-4-8"},
            "3":{"name": "勉強会", "location": "Hack Bar", "date": "2024-5-6"},
            "4":{"name": "サッカーの試合を見に行く", "location": "ノエスタ", "date": "2024-7-20"}
        }
        event = events.get(event_id, None)
        if event:
            name = event["name"]
            location = event["location"]
            date_str = event["date"]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            date_class = "text-danger" if date < datetime.now() else "text-success"
            return render_template("b6-1.html", title=title, name=name, location=location, date=date_str, date_class=date_class)
        else:
            message = "イベントが見つかりません"
            return render_template("b6-1.html", title=title, message=message)
    return render_template("b6-1.html", title=title)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")