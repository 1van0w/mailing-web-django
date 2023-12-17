from django.urls import path
from . import views

urlpatterns = [
    path('mailing-statistics/', views.mailing_statistics_view, name='mailing-statistics'),
    # Добавьте другие URL-маршруты при необходимости
]
