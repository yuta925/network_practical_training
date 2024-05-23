from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

@app.template_filter("days")
def days_filter(time):
    date = datetime.strptime(time, "%Y/%m/%d")
    dt = datetime.now()
    period = date - dt     
    # 残りの日数を返す   
    return period.days + 1

app.jinja_env.filters["days"] = days_filter
# テンプレートフィルタdaysをFlaskアプリケーションに登録する．

@app.route("/")
def timetable():
    return render_template("a3-3.html", title="A3-3", events=events)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")