from django.urls import path

from .views import respondent_search_view, respondent_edit_view, volunteer_cabinet

urlpatterns = [
    path('respondent_search/', respondent_search_view, name='respondent_search'),
    path('respondent_edit/<int:pk>/edit/', respondent_edit_view, name='respondent_edit'),
    path('volunteer_cabinet/', volunteer_cabinet, name="volunteer_cabinet"),
]