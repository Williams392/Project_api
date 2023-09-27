from django.urls import path
from .views import (
    SurveyListCreateView,
    SurveyDetailView,
    OptionListCreateView,
    VoteCreateView,
)

#  surveys(encuestas)
urlpatterns = [
    path('surveys/', SurveyListCreateView.as_view(), name='survey-list-create'),
    path('surveys/<int:pk>/', SurveyDetailView.as_view(), name='survey-create'),
    path('options/', OptionListCreateView.as_view(), name='option-list-create'),
    path('votes/', VoteCreateView.as_view(), name='vote-create'),
]