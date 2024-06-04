import datetime
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024-4-4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024-4-8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024-5-31"}
]

@app.route("/", methods=["GET"])
def input():
    last_event_id = request.cookies.get("last_event_id", "")
    return render_template("a4-1in.html", title="イベント検索", last_event_id=last_event_id)

@app.route("/", methods=["POST"])
def output():
    event_id = request.form["event_id"]
    try:
        id = int(event_id)
        name = events[id - 1].get("name")
        location = events[id - 1].get("location")
        event_date = datetime.datetime.strptime(events[id - 1].get("date"), "%Y-%m-%d")
        current_date = datetime.datetime.now()
        if current_date < event_date:
            date = '<font color="red">{}</font>'.format(event_date.strftime("%Y-%m-%d"))
        else:
            date = event_date.strftime("%Y-%m-%d")
    except ValueError:
        message = "整数値を入力してください"
        return render_template("a4-1out.html", message=message)
    except IndexError:
        message = "有効なidを入力してください"
        return render_template("a4-1out.html", message=message)
    
    response = make_response(render_template("a4-1out.html", name=name, location=location, date=date, message=""))
    response.set_cookie("last_event_id", event_id)
    return response

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
