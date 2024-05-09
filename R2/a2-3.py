from flask import Flask, render_template

app = Flask(__name__)

events = [
    {"name": "新歓", "location": "三田駅近くの居酒屋", "date": "2024/4/4"},
    {"name": "誕生日会", "location": "友達の家", "date": "2024/4/8"},
    {"name": "勉強会", "location": "Hack Bar", "date": "2024/5/6"}
]

@app.route("/id<num>")
# ルートがidで始まる場合に呼び出される．idより後の部分は変数numに代入される．
def page(num):
    try:
        num = int(num)
        name = events[num - 1].get("name")
        location = events[num - 1].get("location")
        if (num == 3): 
            date = '<font color="red">{}</font>'.format( events[num - 1].get("date"))
        else: 
            date = events[num - 1].get("date") 
    except ValueError:
        message = "整数値を入力してください"
        return render_template("a2-3.html", message=message)
    except IndexError:
        message = "有効なidを入力してください"
        return render_template("a2-3.html", message=message)
    return render_template("a2-3.html", name=name, location=location, date=date)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port=5001)