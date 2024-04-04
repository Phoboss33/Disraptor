from django.urls import path
from .views import lending_view, valera_view
from lending.views import LendingView


urlpatterns = [
    path('', lending_view, name='lending'),
    path('valera', valera_view, name='valera'),
    # path('', LendingView.as_view(), name='lending')
]

