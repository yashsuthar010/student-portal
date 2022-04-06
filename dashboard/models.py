from pyexpat import model
from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# that is when user will be deleted then notes will also deleted 
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    # IN sql table wanna show title name
    def __str__(self):
        return self.title  

    # django add extra S in SQL table 
    # so if we want to remove that extra S then
    class Meta:
        # new name
        verbose_name = "notes"
        # previous name
        verbose_name_plural = "notes"

class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

   
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        # new name
        verbose_name = "Todos"
        # previous name
        verbose_name_plural = "Todo"


