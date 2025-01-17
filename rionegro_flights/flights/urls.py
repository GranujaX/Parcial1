from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_flight, name='register_flight'),
    path('list/', views.list_flights, name='list_flights'),
    path('statistics/', views.statistics, name='statistics'),
]
