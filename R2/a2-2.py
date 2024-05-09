import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template():
    dt = datetime.datetime.now()
    message = ''
    if dt.second % 2 == 0:
        message = '<span style="color:red;">今日は{a}時{b}分{c}秒です.</span>'.format(a=dt.hour, b=dt.minute, c=dt.second)
    else:
        message = '今日は{a}時{b}分{c}秒です.'.format(a=dt.hour, b=dt.minute, c=dt.second)

    return render_template("a2-2.html", title="表示テスト", message=message)
    # sample2-2.htmlの{{title}}と{{message}}の部分をそれぞれ置換する．

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port=5001)