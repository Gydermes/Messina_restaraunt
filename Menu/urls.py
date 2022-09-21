from django.urls import path, include
from .views import *


urlpatterns = [
    path('first_course/', first_course),
    path('second_course/', second_course),
    path('snacks/', snacks),
    path('garnish/', garnish),
    path('sweets/', sweets),
    path('beverages/', beverages),
    path('', menu)
    ]