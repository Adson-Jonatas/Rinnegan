# core/urls.py

from django.urls import path
from core.views import sync_views
urlpatterns = [
    path("sincronizar/", sync_views.sync_all, name="sincronizar"),
]
