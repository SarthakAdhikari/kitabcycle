from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import  Response

from ads.models import Ad
# AdType, Book, Category, Conditin, PriceType, Price

from api.v1.serializers.ads import AdSerializer, BookSerializer, PriceSerializer


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()

class AdView(views.APIView):
    def save_books(self, data):
        """
        Save a book to the database

        :param dict data: Contains the data in following format:
        {
            "title": str,
            "description": str,
            "ad_type": str,
            "book": {
                    "name": str,
                    "ISBN": str,
                    "category": str
            },
            "price": {
                    "original": int,
                    "final": int
            },
            "pictures": [str]
        }
        """
        book = BookSerializer(data=data["book"])
        price = PriceSerializer(data=data["price"])
        if book.is_valid() and price.is_valid():
            book = book.save()

        if is_valid:
            return True
        return False

    def post(self, request, *args, **kwargs):
        is_saved = self.save_books(data=request.data)
        return Response({"name": "Sarthak"})

    def create(self, *args):
        print("HI")
        pass
