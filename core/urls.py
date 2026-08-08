from django.urls import path
from .views import home, telegram, site_policy


urlpatterns = [
    path("", home, name="home"),
    path("telegram/", telegram, name="telegram"),
    path("policy/", site_policy, name="site_policy"),
]
