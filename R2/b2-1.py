from flask import Flask, render_template, request

app = Flask(__name__)

exchange_rate = { "usd": 156.13, "eur": 167.21, "cny": 21.56 }

@app.route("/", methods=["GET"])
def input():
    return render_template("b2-1in.html", exchange_rate=exchange_rate)

@app.route("/", methods=["POST"])
def output():
    try:
        currency = request.form.get("currency")
        type = request.form.get("type")
        result = float(currency) * exchange_rate[type]
        message = '{} JPY => {} {}'.format(currency, result, type.upper())
    except KeyError:
        message = "有効な通貨を選択してください"
        print(currency)
    except ValueError:
        message = "数値を入力してください"
    return render_template("b2-1out.html", message=message)

if __name__ == "__main__":
    app.debug = True
    app.run(host="localhost", port=5001)