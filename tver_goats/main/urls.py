from django.urls import path
from .views import index, club, team


app_name = 'main'
urlpatterns = [
    path('', index, name='index'),
    path('club/', club, name='club'),
    path('team/', team, name='team'),
]
