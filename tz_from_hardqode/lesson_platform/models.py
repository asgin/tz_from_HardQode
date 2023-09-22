from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class ProductAccess(models.Model):
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Lesson(models.Model):
    product = models.ManyToManyField('Product', related_name='lessons')
    name = models.CharField(max_length=100)
    link = models.URLField()

class LessonView(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.DO_NOTHING)
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time_watching = models.PositiveIntegerField()
    last_watched = models.DateTimeField()

