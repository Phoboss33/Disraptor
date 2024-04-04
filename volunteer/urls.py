from django.urls import path

from .views import respondent_search_view, respondent_edit_view

urlpatterns = [
    path('respondent_search/', respondent_search_view, name='respondent_search'),
    path('respondent_edit', respondent_edit_view, name='respondent_edit')
]