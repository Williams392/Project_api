from rest_framework import serializers
from .models import Post
from clubs.serializers import MemberSerializer

class PostReadSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'