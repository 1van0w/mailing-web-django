from django.urls import path
from .views import CreateMailingAPIView, ListMailingsAPIView

urlpatterns = [
    path('mailings/create/', CreateMailingAPIView.as_view(), name='create-mailing'),
    path('mailings/', ListMailingsAPIView.as_view(), name='list-mailings'),
]