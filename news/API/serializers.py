from rest_framework import serializers
from news.models import NewsDetail


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields="__all__"