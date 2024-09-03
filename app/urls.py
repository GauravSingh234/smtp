# from .models import book
from .views import bookviewset 
from django.urls import path
from .import views


urlpatterns = [
    path('create/' , bookviewset.as_view()),
    path('' , views.send_email )


]