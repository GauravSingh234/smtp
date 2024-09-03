from django.shortcuts import render ,redirect
from .models import book
from .serializers import bookserializer
from rest_framework import generics
from .utils import send_email_to_client,send_email_with_attachement
from django.conf import settings
import random

# Create your views here.

class bookviewset(generics.CreateAPIView   ,  generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = bookserializer


class bookviewset(generics.DestroyAPIView):
    queryset = book.objects.all()
    serializer_class = bookserializer




def index(request):
    return render(request , 'index.html')
    



def send_email(request):
    
    subject ="This Email is from Django server with attachement."
    message = "Hey Please find the  attach file with this email"
    recipient_list = ['gauravsingh2859@gmail.com' , 'aishubhamit2010@gmail.com']
    file_path = f"{settings.BASE_DIR}/manage.py"
    send_email_with_attachement(subject , message ,recipient_list , file_path )
    return redirect('/') 


def home(request):
    book.objects.create(name = f"shubham-{random.randint(0,99)}")
    return redirect('/')