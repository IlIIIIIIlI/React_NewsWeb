from rest_framework.generics import ListAPIView,RetrieveAPIView
from news.models import NewsDetail
from news.API.serializers import NewsDetailSerializer

class NewsDetailView(ListAPIView):
    queryset=NewsDetail.objects.all()
    serializer_class=NewsDetailSerializer


# we create this for react to extract the news content information
# we need to do the same thing in urls.py
class NewsDetailPage(RetrieveAPIView):
    queryset=NewsDetail.objects.all()
    serializer_class=NewsDetailSerializer



