# -*- coding: utf-8 -*-
"""The app module, which contains the app factory functions."""
from flask import Flask
from mongoengine import connect

from settings import ProdConfig
from views import Ping, Home


def create_app(config_object=ProdConfig):
    """An application factory.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)\

    # connect to database
    connect(
        db=config_object.DB['name'],
        username=config_object.DB['username'],
        password=config_object.DB['password'],
        host=config_object.DB['host'],
        port=config_object.DB['port']
    )

    return app


poe_app = create_app()

# register URLs
poe_app.add_url_rule('/ping', view_func=Ping.as_view('ping'))
poe_app.add_url_rule('/', view_func=Home.as_view('home'))

if __name__ == '__main__':
    poe_app.run(debug=True)
