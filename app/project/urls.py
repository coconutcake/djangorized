from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView
from django.urls import reverse
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@mign.pl"),
      license=openapi.License(name="BSD License"),
      
   ),
   public=True,
   url=settings.SERVER_URL,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   # redirect "/" to swagger
   re_path(r'^$', RedirectView.as_view(url='/core/welcome')),
    
   # admin urls
   path('accounts/', admin.site.urls),
    
   # api urls
   path('api/user/',include('user.urls')),
   path('api-auth/', include('rest_framework.urls')),
    
   # Swager urls
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   #core urls
   path('core/', include('core.urls')),
    
]
