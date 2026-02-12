from django.core.management import BaseCommand
from new_app.models import *
from faker import Faker
import time
 
faker = Faker()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        posts_to_create = []

        start_time = time.time() 
        for _ in range(100):
            post = Post(name = faker.word())
            posts_to_create.append(post)
        Post.objects.bulk_create(posts_to_create)

        end_time = time.time()  
        execution_time = end_time - start_time
        print(f"created 100 posts in {execution_time} seconds")
