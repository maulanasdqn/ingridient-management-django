from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_list, name='ingredient-list'),
    path('<int:pk>/', views.ingredient_detail, name='ingredient-detail'),
]