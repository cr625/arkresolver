from django.urls import path
from . import views

app_name = "resolver"
urlpatterns = [
    path("", views.ARK_list, name="ark_list"),
    path("<int:naan>/<shoulder>/<ark_id>", views.ARK_detail, name="ark_detail"),
]
