from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # include all default authentication urls
    path('', include('django.contrib.auth.urls')),
    # link to view of registration
    path('registraion/', views.registration, name='registration'),
]
