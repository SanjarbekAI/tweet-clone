from django.urls import path

from apps.tweets.views import TweetsListView, RedirectTweetsListView

app_name = 'tweets'

urlpatterns = [
    path('', RedirectTweetsListView.as_view(), name='redirect'),
    path('tweets/', TweetsListView.as_view(), name='list'),
    # path('tweets/edit/<int:pk>/', TweetsUpdateView.as_view(), name='edit'),
    # path('tweets/delete/<int:pk>/', TweetsDeleteView.as_view(), name='delete'),
    # path('tweets/self/', MyTweetsListView.as_view(), name='self'),
]
