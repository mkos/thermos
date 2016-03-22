#!/usr/bin/env python

from thermos import app, db
from thermos.models import User, Bookmark
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="adam", email="adam@example.com", password='test'))
    db.session.add(User(username="eva", email="eva@example.com", password='test'))
    db.session.commit()
    print 'Initialized the database'


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print 'Dropped the database'

if __name__ == '__main__':
    manager.run()

