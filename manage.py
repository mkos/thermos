#!/usr/bin/env python
import os
from thermos import createapp, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


app = createapp(os.getenv('THERMOS_ENV') or 'dev')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

