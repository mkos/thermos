from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = "X\xc9i\xef\xf3'\x8a\xc0\x9d)~\xbbf\x89\xdd,C\x90[\xfe\xa41\xe3\xfd"
bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(url = url,
                          user = "mkos",
                          date = datetime.utcnow()
    ))

def new_bookmarks(num):
    return sorted(bookmarks, key = lambda bm: bm['date'], reverse = True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           new_bookmarks = new_bookmarks(5),
                           title="Title passed from view to template",
                           text="Text passed from view to template")

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmark(url)
        flash('stored bookmark: {}'.format(url))
        return redirect(url_for('index'))

    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
