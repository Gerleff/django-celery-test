"""API URL"""
from django.urls import path

from .views import (PingView, StatusView, AddView, SubstractView)


urlpatterns = [
    path('ping', PingView.as_view()),
    path('add/<uuid:account_id>', AddView.as_view()),
    path('substract/<uuid:account_id>', SubstractView.as_view()),
    path('status/<uuid:account_id>', StatusView.as_view()),
]
