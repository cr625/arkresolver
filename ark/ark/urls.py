from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("c1/", include("resolver.urls", namespace="resolver")),
]
