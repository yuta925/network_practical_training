from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def filewrite():
    with open("out.txt", "a", encoding="utf-8") as file:
        # 追記モードでファイルをオープンする．
        file.write("2020/7/24,東京オリンピック\n")
        # ファイルに1行書き込む．
    return render_template("sample2-2.html", title="ファイルの書き込み", message="書き込み終了")


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port=5001)