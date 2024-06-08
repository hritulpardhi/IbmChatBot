from django.urls import path
from . import watson_api_service
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watson_api/", watson_api_service.watsonApiCall, name="watson_api"),
]