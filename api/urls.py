from django.urls import path
from rest_framework import routers
from api.v1.views.ads import AdViewSet, AdTypeViewSet, PriceTypeViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register('ads', AdViewSet, basename='ads')
router.register('ad_type', AdTypeViewSet, basename='ad_type')
router.register('price_type', AdTypeViewSet, basename='price_type')
router.register('category', AdTypeViewSet, basename='category')

urlpatterns = router.urls
