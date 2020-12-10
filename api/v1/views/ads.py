from rest_framework import viewsets

from ads.models import Ad, AdType, Category, PriceType

from api.v1.serializers.ads import (AdSerializer,
                                    AdTypeSerializer,
                                    CategorySerializer,
                                    PriceTypeSerializer)


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()


class AdTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AdTypeSerializer
    queryset = AdType.objects.all()


class PriceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = PriceTypeSerializer
    queryset = PriceType.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
