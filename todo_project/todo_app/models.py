from django.db import models

# Create your models here.

class ToDoItems(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=100)