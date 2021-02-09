from django.db import models
from django.contrib.auth.models import User

MOOD_CHOICES = (
    ("Good","Good"),
    ("Bad","Bad")
)

SESSION_CHOICES = (
    ("Morning","Morning"),
    ("Afternoon","Afternoon"),
    ("night","night")
)

CATEGORY_CHOICES = (
    ("WakeUp","WakeUp"),
    ("Studies","Studies"),
    ("My Work","My Work"),
    ("Entertainment","Entertainment"),
    ("Political_News","Political_News"),
    ("Bussiness_Decions","Bussiness_Decions"),
)
class Items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    date= models.DateField(auto_now_add=set,null=True,blank=True)
    feedback=models.CharField(max_length=120,choices=MOOD_CHOICES,blank=True)
    description = models.TextField(blank=True,null=True)
    session = models.CharField(max_length=120,choices=SESSION_CHOICES , blank=True)
    time = models.TimeField(blank=True,null=True)
    category = models.CharField(blank=True,choices=CATEGORY_CHOICES,max_length=400)


class ToDoItems(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(blank=True,null=True)
    description = models.TextField(blank=True, null=True)




