from django.shortcuts import render
from rest_framework.response import responses
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializer import *

class LocaisDescarteListCreate(ListCreateAPIView):
    queryset = LocaisDescarte.objects.all()
    serializer_class = LocaisDescarteSerializer

class LocaisDescarteDetail(RetrieveUpdateDestroyAPIView):
    queryset = LocaisDescarte.objects.all()
    serializer_class = LocaisDescarteSerializer