from django.urls import path
from elections import views
urlpatterns = [
    path('', views.home, name='home'),
]
