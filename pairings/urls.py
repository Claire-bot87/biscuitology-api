from django.urls import path 
from .views import PairingListView, PairingDetailView

urlpatterns = [
path('', PairingListView.as_view()),
path('<int:pk>/', PairingDetailView.as_view())

]