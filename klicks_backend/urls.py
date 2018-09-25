from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token
# from django.contrib.auth.views import login

from api.views import EventViewSet, CategoryViewSet, TagViewSet, GroupViewSet

router = SimpleRouter()
# router.register('profiles', UserProfileViewSet, base_name='profile')
router.register('events', EventViewSet, base_name='events')
router.register('categories', CategoryViewSet, base_name='categories')
router.register('tags', TagViewSet, base_name='tags')
router.register('groups', GroupViewSet, base_name='groups')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # route for user signup
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('token-auth/', obtain_jwt_token),
    path('api/', include('api.urls')),
]
