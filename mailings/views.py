from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Mailing
from .serializers import MailingSerializer

class CreateMailingAPIView(generics.CreateAPIView):
    serializer_class = MailingSerializer



class ListMailingsAPIView(generics.ListAPIView):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer