from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_triangle, name='check_triangle'),
]