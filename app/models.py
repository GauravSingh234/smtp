from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField(null=True)

@receiver(post_save , sender = book) 
def call_book_api(sender , instance , **kwargs) :
    print("BOOK OBJECT CREATED")
    print(sender , instance , kwargs)
    

book(name= "shubham")
book(name= "rohit")    
