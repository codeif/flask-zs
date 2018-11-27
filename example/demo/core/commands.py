import click
from flask.cli import with_appcontext

from . import db
from ..models.user import User


def init_db():
    db.create_all()

    for name, phone in [
        ('张三', '15212451234'),
        ('李四', '13412451234'),
    ]:
        user = User(name=name, phone=phone)
        db.session.add(user)

    db.session.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.cli.add_command(init_db_command)
