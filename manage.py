# -*- coding: utf-8 -*-

from cloud import app, db
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from cloud.user import User, USER_ADMIN, USER_NORMAL

from cloud import create_app

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command( 'db' , MigrateCommand )
manager.add_command( 'runserver' , Server(host='0.0.0.0') )


@manager.command
def run():
    """Run in local machine."""
    app.run(host='0.0.0.0', debug=True, port=5000)
    # app.run()

@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    admin = User(
            name=u'admin',
            password=u'123456',
            type_code=USER_ADMIN)
    demo = User(
            name=u'demo',
            password=u'123456',
            type_code=USER_NORMAL)
    db.session.add(admin)
    db.session.add(demo)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
