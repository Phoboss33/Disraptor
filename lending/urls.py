from django.urls import path

from lending.views import testform

urlpatterns = [
    path('', testform, name='test_form'),
]

