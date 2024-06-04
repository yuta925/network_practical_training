import re

# 正規表現モジュールのインポート
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
# 入力画面の表示
def regular_expression():
    return render_template("sample4-1.html", title="アドレス帳検索")


@app.route("/", methods=["POST"])
# 出力画面の表示
def phone():
    number = request.form["number"]
    with open("data.txt", encoding="utf-8") as file:
        data = []
        for text in file:
            item = text.split(",")
            if re.search(number, item[3]):
                # 正規表現を用いて電話番号(item[3])を検索し，ヒットしたものをdataに追加する．
                data.append(item)
    return render_template("sample4-1.html", title="アドレス帳検索", data=data, num=number)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")
