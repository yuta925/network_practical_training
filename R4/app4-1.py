from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "abc"
# セッション変数を利用するためには秘密鍵(secret_key)の登録が必要

@app.route("/")
def count_session():
    if "count" in session:
        # "count"という名前のセッション変数を探す．
        count = session["count"]
        # あれば変数countに代入する
    else:
        # なければ変数countを1に初期化する．
        count = 1

    message = "あなたはこのサイトに{}回アクセスしました．".format(count)
    session["count"] = count + 1
    # セッション変数を1増やして，更新する．
    return render_template("sample2-2.html", title="セッション変数", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port="5001")
