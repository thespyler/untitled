from django.db import models

class Question(models.Model):
	question = models.TextField(max_length=1000)
# Create your models here.
class Users(models.Model):
	name = models.TextField(max_length=100)