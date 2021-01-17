from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    email= models.EmailField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=set,null=True)

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ("SmartPhone","SmartPhone"),
    ("Laptop","Laptop"),
    ("Tv","Tv"),
    ("Hometheather",'Hometheater'),
    ("Desktop","Desktop")
)
class Products(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    qtn = models.CharField(max_length=5,blank=True,null=True)
    category = models.CharField(max_length=40,blank=True,null=True,choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=set, null=True)
    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ('dilivered','dilivered'),
    ('out of dilivery','out of dilivery'),
    ('pending','pending'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    product =  models.ForeignKey(Products,on_delete=models.SET_NULL,blank=True,null=True)
    status = models.CharField(max_length=200,blank=True,null=True,choices=STATUS_CHOICES)
    date_created =models.DateTimeField(auto_now_add=set,null=True)
    note = models.CharField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return f"{self.customer}-{self.product}"