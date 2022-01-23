from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.db.models import F 

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoViewByDate(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all().order_by(F('date').asc(nulls_last = True))