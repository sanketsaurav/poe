import datetime
import uuid
from mongoengine import Document, StringField, DateTimeField, signals

from utils import slugify


class Post(Document):
    """
    Mongo document schema for a post.
    """
    title = StringField(max_length=255)
    author = StringField(max_length=128)
    content = StringField()
    slug = StringField(max_length=255, unique=True)
    modified = DateTimeField(default=datetime.datetime.now)
    secret_key = StringField(max_length=255)

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.slug = slugify(document.title)

        # exit if this is an update, not creation
        if document.pk:
            return

        # ensure a unique slug for this post
        counter = 1
        new_slug = document.slug
        while sender.objects.filter(slug=new_slug).limit(1).count(True):
            new_slug = "{}-{}".format(document.slug, counter)
            counter += 1
        document.slug = new_slug

        # create a secret key for this post
        document.secret_key = uuid.uuid4().hex


signals.pre_save.connect(Post.pre_save, sender=Post)
