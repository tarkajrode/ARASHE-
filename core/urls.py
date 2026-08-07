from django.urls import path
from .views import home, telegram


urlpatterns = [
    path("", home, name="home"),
    path("telegram/", telegram, name="telegram"),
]
