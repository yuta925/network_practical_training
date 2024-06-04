from flask import Flask, request, render_template, make_response
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    event_name = request.cookies.get('event_name', '')
    event_date = request.cookies.get('event_date', '')
    message = None
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_date_dt = datetime.strptime(event_date, '%Y-%m-%d')
        today = datetime.today()
        days_left = (event_date_dt - today).days
        message = f"{event_name}まで、あと{days_left}日です。"

        response = make_response(render_template('b4-2.html', event_name=event_name, event_date=event_date, message=message))
        response.set_cookie('event_name', event_name, max_age=60*60*24*30)
        response.set_cookie('event_date', event_date, max_age=60*60*24*30)
        return response

    return render_template('b4-2.html', event_name=event_name, event_date=event_date, message=message)

if __name__ == '__main__':
    app.run(debug=True)
