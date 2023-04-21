from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

class Post(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    date = models.DateField()