from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers
from customers.views import CustomerViewSet
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


TITILE = "Magic app"
schema_view = get_schema_view(
   openapi.Info(
      title=TITILE,
      default_version='v1',
      description="Test description",
   ),
   validators=['flex', 'ssv'],
   public=True,
)


router = routers.SimpleRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title=TITILE)),
    re_path(r'^schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^openapi/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-swagger-ui'),
] + router.urls
