from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(is_published = True)
    # def recent(self):
    #     return self.get_queryset().filter(created_at = ) # ვერ გავაკეთე
    def with_comment(self):
        return self.get_queryset().filter(comments__isnull = False).distinct()

class CommentManager(models.Manager):
    def for_post(self, post):
        post_type = ContentType.objects.get_for_model(Post)
        return self.get_queryset().filter(content_type=post_type, object_id=post.id)
    # def recent(self):
    #     return self.get_queryset().filter(created_at =) #ვერ გავაკეთე

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    comments = GenericRelation("Comment", related_query_name="post")
    images = GenericRelation("Image", related_query_name="post")
    objects = PostManager()

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    bio = models.TextField()
    images = GenericRelation("Image", related_query_name="author")

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = CommentManager()

    def __str__(self):
        return self.text


class Image(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.description
