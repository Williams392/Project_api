from django.db.models import Prefetch, OuterRef, Subquery
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Image, Video, Member
from .serializers import PostSerializer, PostReadSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.parsers import JSONParser
from django.http import Http404
# Create your views here.

class PostView(APIView):

    def get(self, request):
        club_id = request.query_params.get('club-id', None)
        user_id = request.query_params.get('user-id', None)
        queryset = Post.objects.all().order_by('-timestamp')

        if club_id:
            queryset = queryset.filter(member__club_id=club_id)
        elif user_id:
            queryset = queryset.filter(member__profile__user__pk=user_id)

        posts_with_images = queryset.prefetch_related(
            Prefetch('images', queryset=Image.objects.all(), to_attr='all_images'),
            Prefetch('videos', queryset=Video.objects.all(), to_attr='all_videos')
        )

        response = []
        for post in posts_with_images:
            post_data = {
                'post_id': str(post.id),
                'full_name': str(post.member.profile),
                'first_name': post.member.profile.user.first_name,
                'last_name': post.member.profile.user.last_name,
                'user_id': post.member.profile.user.pk,
                'user_photo': str(post.member.profile.profile_picture),
                'content': post.content
            }
            post_data['photos'] = [{'image': str(image.image)} for image in post.all_images]
            post_data['videos'] = [{'video': str(video.video)} for video in post.all_videos]
            response.append(post_data)

        return Response(response)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)