from django.urls import path
from .views import lending_view


urlpatterns = [
    path('', lending_view, name='lending'),
]

