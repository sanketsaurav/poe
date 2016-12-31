# -*- coding: utf-8 -*-
"""The app module, which contains the app factory functions."""
from flask import Flask
from mongoengine import connect

from settings import ProdConfig
from views import HomeView, PostView, RandomView


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
        port=config_object.DB['port'],
        alias='default'
    )

    return app


poe_app = create_app()

# register URLs
poe_app.add_url_rule('/', view_func=HomeView.as_view('home'))
poe_app.add_url_rule('/random', view_func=RandomView.as_view('random'))
poe_app.add_url_rule('/<path>', view_func=PostView.as_view('post'))


# add a template filter
@poe_app.template_filter()
def format_date(date):
    return date.strftime("%b %d, %Y")


if __name__ == '__main__':
    poe_app.run(debug=True)
