from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/")
def get():
    return render_template("a3-2.html", title="A3-2", collections=collections)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")