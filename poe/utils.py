# -*- coding: utf-8 -*-
"""Borrowed from http://flask.pocoo.org/snippets/5/"""
import re

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(word.split())
    return delim.join(result)
