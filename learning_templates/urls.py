from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from basic_app import views

urlpatterns = [
    # Admin Page
    path("admin/", admin.site.urls),
    # Home Page
    path("", views.index, name="index"),
    # Base URL to basic_app
    path("basic_app/", include("basic_app.urls")),
]
