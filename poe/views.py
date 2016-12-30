# -*- coding: utf-8 -*-
"""View functions for Poe."""
from flask.views import MethodView
from flask import render_template


class Ping(MethodView):
    def get(self):
        return "PONG"


class Home(MethodView):
    """
    View for rendering the home page of the app.
    On GET: Render the home page.
    On POST: Create a new post, and redirect to the post's page.
    """
    def get(self):
        return render_template('home.html')

    def post(self):
        pass


class Post(MethodView):
    def get(self):
        pass
