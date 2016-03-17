from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import BookmarkForm
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "X\xc9i\xef\xf3'\x8a\xc0\x9d)~\xbbf\x89\xdd,C\x90[\xfe\xa41\xe3\xfd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)

import models


# Fake login for now
def logged_in_user():
    return models.User.query.filter_by(username='adam').first()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           new_bookmarks=models.Bookmark.newest(5),
                           title="Title passed from view to template",
                           text="Text passed from view to template")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data

        bm = models.Bookmark(user=logged_in_user(), url=url, description=description)
        db.session.add(bm)
        db.session.commit()

        flash('stored bookmark: {}'.format(description))
        return redirect(url_for('index'))

    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
