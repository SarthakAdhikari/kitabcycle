from django.urls import path
from rest_framework import routers
from api.v1.views.ads import AdViewSet, AdView

router = routers.SimpleRouter()

router.register('ads', AdViewSet, basename='ads')

urlpatterns = router.urls

urlpatterns += [
    path('create-ad', AdView.as_view(), name='create_ad'),
]
