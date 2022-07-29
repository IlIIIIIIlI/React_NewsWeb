from django.urls import path
from news.API.views import NewsDetailView, NewsDetailPage

urlpatterns = [
    path("news", NewsDetailView.as_view()),
    # for example, if we go to 127.0.0.1/api/news/1238128907, we get the id's content
    path("news/<int:pk>", NewsDetailPage.as_view()),
]

