# -*- coding: utf-8 -*-
"""View functions for Poe."""
from flask.views import MethodView
from flask import render_template


class Ping(MethodView):
    def get(self):
        return "PONG"


class Home(MethodView):
    def get(self):
        return render_template('home.html')
