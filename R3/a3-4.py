from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

@app.context_processor
# コンテキストプロセッサの定義
def caluculate():
    def days_filter(time):
        date = datetime.strptime(time, "%Y/%m/%d")
        dt = datetime.now()
        period = date - dt     
        # 残りの日数を返す   
        return period.days + 1
    return dict(days_filter=days_filter)

@app.route("/")
def timetable():
    return render_template("a3-4.html", title="A3-4", events=events)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)