# -*- coding: utf-8 -*-
"""
Add Documentation Here
"""

from flask import Flask

from .globals import mail, migrate, api

from server.core.admin import admin_api, user_api, role_api
from server.core.loans import loans_api


def create_app(settings_override=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(settings_override)

    register_appliances(app)

    register_namespaces(app)

    register_cli(app)

    register_teardowns(app)

    return app


def register_appliances(app):

    mail.init_app(app)

    migrate.init_app(app)


def register_namespaces(app):

    # Admin namespace
    api.add_namespace(admin_api, path='/api/v1/admin')
    api.add_namespace(user_api, path='/api/v1/users')
    api.add_namespace(role_api, path='/api/v1/roles')

    # Loans namespace
    api.add_namespace(loans_api, path='/api/v1/loans')

    # Finally initialize the Api
    api.init_app(app)


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
