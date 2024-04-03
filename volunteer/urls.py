from django.urls import path

from .views import respondent_search_view

urlpatterns = [
    path('respondent_search/', respondent_search_view, name='respondent_search'),
]