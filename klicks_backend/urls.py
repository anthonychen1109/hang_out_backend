from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import (
    UserViewSet,
    LocationViewSet,
    EventViewSet
)

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
