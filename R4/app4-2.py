from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route("/")
def cookie():
    count = request.cookies.get("count")
    # クッキー変数"count"を読み出し，countに代入する．
    if count is None:
        # クッキー変数"count"が存在しない場合は，countに"1"を代入する．
        count = "1"
    message = "あなたはこのサイトに{}回アクセスしました．".format(count)
    max_age = 60 * 60 * 24 * 120
    # クッキーの賞味期限を120日にする
    response = make_response(render_template("sample2-2.html", title="クッキーの利用", message=message))
    response.set_cookie("count", value=str(int(count) + 1), max_age=max_age)
    # クッキー変数"count"にcountに1加えたものを代入する．
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port="5001")