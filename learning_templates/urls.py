from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from basic_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Home Page
    path("", views.index, name="index"),
    path("/basic_app/", include("basic_app.urls")),
]
