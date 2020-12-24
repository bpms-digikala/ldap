
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ReferenceViewSet, ManagerViewSet, PartnerViewSet

router = routers.DefaultRouter()
router.register('reference', ReferenceViewSet)
router.register('manager', ManagerViewSet)
router.register('partner', PartnerViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
