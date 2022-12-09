from nikita import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('error', views.error),
]
