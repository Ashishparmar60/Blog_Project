from django.db import models
from uuid import uuid4


# Create your models here.
class User(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid4)
    password = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

class Person(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Blog(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)


