from rest_framework import serializers
from .models import book



class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['name' , 'author' , 'price']

