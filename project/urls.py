from django.contrib import admin
from django.urls import path, include
from users.views.views import HomeStub

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('users/', include('users.urls')),
    path('api/v0/', include('api_v0.urls')),
    path('lending/', include('lending.urls')),
    path('volunteer/', include('volunteer.urls')),
    path('', HomeStub.as_view(), name='homepage'),
]
