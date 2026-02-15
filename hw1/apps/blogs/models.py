from django.db.models import (
    Model,
    CharField,
    SlugField,
    ForeignKey,
    CASCADE,
    TextField,
    SET_NULL,
    ManyToManyField,
    DateTimeField
)


class Category(Model):
    name = CharField(max_length=100, unique=True)
    slug = SlugField(max_length=100, unique=True)


class Tag(Model):
    name = CharField(max_length=50, unique=True)
    slug = SlugField(max_length=100, unique=True)


class Post(Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    author = ForeignKey('users.User', on_delete=CASCADE)
    title = CharField(max_length=200)
    slug = SlugField(max_length=100, unique=True)
    body = TextField()
    category = ForeignKey(Category, on_delete=SET_NULL, null=True)
    tags = ManyToManyField(Tag, blank=True)
    status = CharField(max_length=20, choices=STATUS_CHOICES)
    inserted_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE, related_name="comments")
    author = ForeignKey('users.User', on_delete=CASCADE)
    body = TextField()
    inserted_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
