from django.urls import path
from api import views

urlpatterns = [
    path('get-data', views.GetDataAPIView.as_view(), name="get-data"),
]
