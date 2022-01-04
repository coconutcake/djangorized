from django.urls import path, include, re_path



from core import views
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from rest_framework.schemas import get_schema_view

app_name = 'core'

urlpatterns = [

    re_path(r"^welcome/$", views.WelcomeView.as_view(), name="Welcome"),
    

]

