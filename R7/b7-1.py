from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'b7-1.db'    

# データベース接続の設定
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return render_template('b7-1.html', books=books)

@app.route('/search', methods=['GET'])
def search():
    search_term = request.args.get('search')
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + search_term + '%',))
    books = cursor.fetchall()
    conn.close()
    return render_template('b7-1.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    published_year = request.form['published_year']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, genre, published_year) VALUES (?, ?, ?, ?)", 
                   (title, author, genre, published_year))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host="localhost")
