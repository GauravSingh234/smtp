from django.shortcuts import render ,redirect
from .models import book
from .serializers import bookserializer
from rest_framework import generics
from .utils import send_email_to_client


# Create your views here.

class bookviewset(generics.CreateAPIView   ,  generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = bookserializer




    



def send_email(request):
    send_email_to_client()
    return render(request , "index.html")    