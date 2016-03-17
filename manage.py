#!/usr/bin/env python

from thermos.thermos import app, db
from flask.ext.script import Manager, prompt_bool
from thermos.models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="adam", email="adam@example.com"))
    db.session.add(User(username="eva", email="eva@example.com"))
    db.session.commit()
    print 'Initialized the database'


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()

