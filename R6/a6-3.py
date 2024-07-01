from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])

def sample():
    return render_template("a6-3.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost")