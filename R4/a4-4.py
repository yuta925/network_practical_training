from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def fileupload():
    return render_template("a4-4.html")


@app.route("/", methods=["POST"])
def filewrite():
    message = ""
    event_date = request.form["event_date"]
    event_name = request.form["event_name"]
    with open("a4-3.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{event_date},{event_name}")
    message = "書き込み終了"
    return render_template("a4-4.html", message=message)


if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")