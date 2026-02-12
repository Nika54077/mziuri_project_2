from django.core.management import BaseCommand
from django.db import transaction
from new_app.models import Post, Image, Comment
from faker import Faker

faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        def create_post_with_images(fail=False):
            try:
                with transaction.atomic():
                    post = Post.objects.create(
                        title=faker.word() if not fail else None,
                        content=faker.text()
                    )

                    for _ in range(3):
                        Image.objects.create(post=post, url=faker.image_url())

                    for _ in range(2):
                        Comment.objects.create(post=post, content=faker.sentence())

                    print("Done")
                    return post

            except Exception:
                print("Failed")
                return None

        print("Success test:")
        create_post_with_images(fail=False)

        print("Fail test:")
        create_post_with_images(fail=True)
