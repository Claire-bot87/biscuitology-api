from django.urls import path
from .views import BiscuitListView, BiscuitDetailView


urlpatterns = [

    path('', BiscuitListView.as_view()),
    path('<int:biscuit_id>/', BiscuitDetailView.as_view())

]
