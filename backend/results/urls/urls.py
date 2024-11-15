from django.urls import path
from results.views.results import ResultsView

urlpatterns = [
    path('results/', ResultsView.as_view(), name='results'),
]