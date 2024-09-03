# from .models import book
from .views import bookviewset 
from django.urls import path
from .import views


urlpatterns = [
    path('create/' , bookviewset.as_view()),
    path('send_email/' , views.send_email , name = "send_email" ),
    path('' , views.index , name = "index" ),
    path('home/' , views.home , name = "home" ),





]