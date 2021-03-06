# -*- coding: utf-8 -*-
"""View functions for Poe."""
from flask.views import MethodView
from flask import render_template, request, jsonify

from models import Post


class HomeView(MethodView):
    """
    View for rendering the home page of the app.
    On GET: Render the home page.
    On POST: Create a new post, and redirect to the post's page.
    """
    def get(self):
        return render_template('home.html')

    def post(self):
        data = request.get_json()
        print(data)
        new_post = Post(**data)
        new_post.save()
        return jsonify({
            'slug': new_post.slug
        })


class PostView(MethodView):
    """
    View for posts.
    On GET: Render detail view for a post.
    On POST: Update the details of a post.
    """
    def get(self, path):
        try:
            post = Post.objects.get(slug=path)
            return render_template('post.html', post=post)
        except:
            return render_template('404.html'), 404

    def post(self, path):
        pass


class RandomView(MethodView):
    def get(self):
        pass
