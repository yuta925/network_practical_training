from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def table():
    name = ["北村一輝", "高橋一生", "藤原竜介"]
    return render_template("sample6-4.html", title="教員名簿", name=name)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)