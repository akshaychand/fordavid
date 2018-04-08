# -*- coding: utf-8 -*-
"""
Add Documentation Here
"""

from flask import Flask, Blueprint

from .globals import mail, migrate, api


def create_app(settings_override=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings_override)

    register_appliances(app)

    register_routes(app)

    register_cli(app)

    register_teardowns(app)

    return app


def register_appliances(app):

    mail.init_app(app)

    migrate.init_app(app)


def register_routes(app):
    """
    Register all route modules
    """
    api.init_app(app, title='')
    api_master_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(api_master_blueprint)

    # for name in find_modules('flaskr.blueprints'):
    #     mod = import_string(name)
    #     if hasattr(mod, 'bp'):
    #         app.register_blueprint(mod.bp)
    return None


def register_cli(app):

    @app.cli.command('initdb')
    def initdb_command():
        """
        Creates the database tables.
        """
        None


def register_teardowns(app):

    @app.teardown_appcontext
    def close_db(error):
        """
        Closes the database again at the end of the request.
        """
        None
