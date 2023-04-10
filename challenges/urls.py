from django.urls import path
from . import views

"""urlpatterns = [
    path('', views.challenges_main),
    path('january', views.january_challenge),
    path('february', views.february_challenge),
]
"""


urlpatterns = [
    path('', views.challenges_main),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge),
]
