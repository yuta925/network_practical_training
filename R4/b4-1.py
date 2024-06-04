from flask import Flask, request, render_template
import re

app = Flask(__name__)

# イベントデータをファイルから読み込む関数
def load_events():
    with open('a4-3.txt', 'r', encoding='utf-8') as file:
        events = file.readlines()
    return events

# イベントを検索する関数
def search_events(year, month, day):
    events = load_events()
    filtered_events = []
    for event in events:
        match = True
        if year and not re.search(f'{year}', event):
            match = False
        if month and not re.search(f'{month}', event):
            match = False
        if day and not re.search(f'{day}', event):
            match = False
        if match:
            filtered_events.append(event.strip())
    return filtered_events

@app.route('/')
def index():
    return render_template('b4-1in.html')

@app.route('/search', methods=['POST'])
def search():
    year = request.form.get('year')
    month = request.form.get('month')
    day = request.form.get('day')
    events = search_events(year, month, day)
    return render_template('b4-1out.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)

