from django.urls import path
from . import views

app_name = "resolver"
urlpatterns = [
    path("", views.ARKListView.as_view(), name="ark_list"),
    path("<ark_id>/", views.ARK_detail, name="ark_detail"),
]
