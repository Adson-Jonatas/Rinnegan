from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('', admin.site.urls),
    path("set_language/", set_language, name="set_language"),
    path("core/", include("core.urls")),
]