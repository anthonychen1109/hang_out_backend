from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token
# from django.contrib.auth.views import login

from api.views import UserViewSet, EventViewSet, CategoryViewSet, TagViewSet, GroupViewSet

router = SimpleRouter()
router.register('profiles', UserViewSet, base_name='profile')
router.register('events', EventViewSet, base_name='events')
router.register('categories', CategoryViewSet, base_name='categories')
router.register('tags', TagViewSet, base_name='tags')
router.register('groups', GroupViewSet, base_name='groups')

API_TITLE = 'Hang Outs'
API_DESCRIPTION = 'A meetup planner'
schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # for easy admin login/ logout
    path('api-auth/', include('rest_framework.urls')),
    # route for log-in, log-out, password reset API endpoints
    # path('api/v1/rest-auth/', include('rest_auth.urls')),
    # route for user signup
    # path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('yth', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view),
    path('token-auth/', obtain_jwt_token),
    path('api/', include('api.urls'))
    # path('api-token-auth/', obtain_auth_token),

]
