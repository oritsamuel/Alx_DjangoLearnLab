from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


# Create your views here.
from rest_framework import generics
from rest_framework import viewsets, permissions
from .serializers import BookSerializer
from .models import Book

class BookList(generics.ListAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAdminUser]  # Require admin user
    permission_classes = [IsAuthenticated]