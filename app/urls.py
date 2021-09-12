from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cssShapes/', views.cssShapes),
    path('jsLoops/', views.jsLoops),
    path('jsConditionals/', views.jsConditionals),
    path('flexbox/', views.flexbox),
]