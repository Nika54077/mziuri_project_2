from django.core.management import BaseCommand
from new_app.models import Post

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        posts_many_comments = [p for p in Post.objects.all() if p.comment_set.count() > 5]
        for p in posts_many_comments:
            print(p.title)

        posts_author_john = Post.objects.filter(author__name__icontains="john")
        for p in posts_author_john:
            print(p.title)

        posts_with_images = Post.objects.filter(is_published=True).exclude(image_set=None)
        for p in posts_with_images:
            print(p.title)
