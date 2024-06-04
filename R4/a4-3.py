from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d'):
    return datetime.strptime(value, format)
    
@app.route('/')
def address():
    with open("a4-3.txt", encoding="utf-8") as file:
        data = []
        for text in file: 
            data.append(text.split(","))
        schema = ["日付", "イベント名"]
    current_date = datetime.now().strftime("%Y-%m-%d")
    return render_template("a4-3.html", title="イベント一覧", schema=schema, table=data, current_date=current_date)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')