from rest_framework import routers
from django.contrib import admin
from django.urls import include, path
from app.urls import urlpatterns as api_urls
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'authors', views.AuthorsViewsSet)
#path('q1/',include('question1.urls')),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_urls), name="api"),
    path('api_schema/', get_schema_view(title='API Schema', description='Guide for REST API'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(template_name='swagger-ui.html',    extra_context={'schema_url':'api_schema'}), name='swagger-ui'),
    path('', include(router.urls))
]


