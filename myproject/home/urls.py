from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home, name='homepage'),
    path('other/', other, name='otherpage'),
    path('about/', about, name='aboutpage'),
]