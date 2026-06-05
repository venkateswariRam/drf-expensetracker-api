from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Expense(models.Model):
    title=models.CharField(max_length=100)
    amount=models.IntegerField()
    category=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)