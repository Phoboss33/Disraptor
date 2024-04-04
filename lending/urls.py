from django.urls import path
from .views import lending_view, valera_view


urlpatterns = [
    path('', lending_view, name='lending'),
    path('valera', valera_view, name='valera')
]

