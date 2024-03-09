from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name


# Create your models here.
class webpage(models.Model):
    topic_name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
