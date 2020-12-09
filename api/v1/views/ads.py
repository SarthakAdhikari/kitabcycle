from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import  Response

from ads.models import Ad
# AdType, Book, Category, Conditin, PriceType, Price

from api.v1.serializers.ads import AdSerializer, BookSerializer, PriceSerializer


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
