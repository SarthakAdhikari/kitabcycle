from django.urls import path
from rest_framework import routers
from api.v1.views.ads import AdViewSet

router = routers.SimpleRouter()

router.register('ads', AdViewSet, basename='ads')

urlpatterns = router.urls
