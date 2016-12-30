import datetime
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

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        document.slug = slugify(document.title)

        # check if a post with this slug already exists
        counter = 1
        new_slug = document.slug
        while sender.objects.filter(slug=new_slug).limit(1).count(True):
            new_slug = "{}-{}".format(document.slug, counter)
            counter += 1
        document.slug = new_slug


signals.pre_save.connect(Post.pre_save, sender=Post)
