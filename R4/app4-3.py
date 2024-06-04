from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def address3a():
    with open("data.txt", encoding="utf-8") as file:
        data = []
        for text in file:
            # ファイルから１行づつ読み出し，textに代入する
            data.append(text.split(","))
            # textを","で分割し，リストとしたものをdataに加える．
        schema = ["No.", "名前", "性別", "電話番号", "住所"]
    return render_template("sample3-1.html", title="住所録一覧", schema=schema, table=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost",port=5001)