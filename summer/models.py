from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=30000)

