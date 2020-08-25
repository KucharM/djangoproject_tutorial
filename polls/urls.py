from django.urls import path
from .views import IndexView, PollResultView, PollDetailView, vote


app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PollDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', PollResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', vote, name='vote'),
]