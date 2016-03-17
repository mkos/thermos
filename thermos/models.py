from datetime import datetime
from thermos import db
from sqlalchemy import desc


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # passing reference to function instead of result of the
                                                            # function. That way it will be called every time record
                                                            # is added rather than always having the same value
    description = db.Column(db.String(300))

    def __repr__(self):
        return "<Bookmark: '{}': '{}'>".format(self.description, self.url)

    @staticmethod
    def newest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return "<User %r>" % self.username