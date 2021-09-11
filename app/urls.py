from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('cssShapes/', views.cssShapes),
]