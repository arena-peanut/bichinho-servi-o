from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/create/', views.create_bichinhos, name='create'),
    path('/list/', views.list, name='list'),
]
