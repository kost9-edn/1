from django.urls import path
from .views import test_viev

urlpatterns = [
    path('', test_viev, name='base')
]
