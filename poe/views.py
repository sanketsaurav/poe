# -*- coding: utf-8 -*-
"""View functions for Poe."""
from flask.views import MethodView


class Ping(MethodView):
    def get(self):
        return "PONG"
