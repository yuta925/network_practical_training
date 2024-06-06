from flask import Flask, render_template, request, flash
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # フラッシュメッセージ用のシークレットキー

# フィルタ: 日付に対して学期を判断する
@app.template_filter('semester')
def semester(date):
    spring_start = datetime(2024, 4, 8)
    spring_end = datetime(2024, 7, 19)
    autumn_start_1 = datetime(2024, 10, 20)
    autumn_end_1 = datetime(2024, 12, 23)
    autumn_start_2 = datetime(2025, 1, 6)
    autumn_end_2 = datetime(2025, 1, 9)

    if spring_start <= date <= spring_end:
        return "春学期中"
    elif autumn_start_1 <= date <= autumn_end_1 or autumn_start_2 <= date <= autumn_end_2:
        return "秋学期中"
    else:
        return "授業期間外"

# コンテキストプロセッサ: 授業終了日までの日数を計算する
@app.context_processor
def countdown():
    def get_days_until_end(date):
        spring_end = datetime(2024, 7, 19)
        autumn_end_1 = datetime(2024, 12, 23)
        autumn_end_2 = datetime(2025, 1, 9)

        autumn_start_1 = datetime(2024, 10, 20)
        autumn_start_2 = datetime(2025, 1, 6)

        if date <= spring_end:
            delta = spring_end - date
        elif autumn_start_1 <= date <= autumn_end_1:
            delta = autumn_end_1 - date
        elif autumn_start_2 <= date <= autumn_end_2:
            delta = autumn_end_2 - date
        else:
            delta = None

        if delta:
            return delta.days
        return None

    return dict(get_days_until_end=get_days_until_end)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        month_str = request.form['month']
        day_str = request.form['day']

        # バリデーション: 月と日の値が有効かどうかを確認
        if not re.match(r"^\d{1,2}$", month_str) or not re.match(r"^\d{1,2}$", day_str):
            flash("月と日は数字で入力してください。", "error")
            return render_template('b3-2in.html')
        
        month = int(month_str)
        day = int(day_str)

        # 月が1から12の範囲内かどうかを確認
        if month < 1 or month > 12:
            flash("月は1から12の範囲で入力してください。", "error")
            return render_template('b3-2in.html')

        # 日が1から31の範囲内かどうかを確認
        if day < 1 or day > 31:
            flash("日は1から31の範囲で入力してください。", "error")
            return render_template('b3-2in.html')

        try:
            date = datetime.strptime(f"2024-{month_str}-{day_str}", '%Y-%m-%d')
        except ValueError:
            flash("無効な日付です。", "error")
            return render_template('b3-2in.html')

        return render_template('b3-2out.html', date=date)
    
    return render_template('b3-2in.html')

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5001)
