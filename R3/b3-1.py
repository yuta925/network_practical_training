from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get():
    collections = [
    {
        "name": "新歓",
        "location": "三田駅近くの居酒屋",
        "date": "2024-04-04"
    },
    {
        "name": "誕生日会",
        "location": "友達の家",
        "date": "2024-04-08"
    },
    {
        "name": "ヴィッセル神戸",
        "location": "茨城県立カシマサッカースタジアム",
        "date": "2024-05-19"
    }
    ]
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template("b3-1.html", title="B3-1", collections=collections, current_date=current_date)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")