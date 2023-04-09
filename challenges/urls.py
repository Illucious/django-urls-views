from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenges_main),
    path('january', views.january_challenge),
    path('february', views.february_challenge),

]
