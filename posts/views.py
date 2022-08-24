from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *

class PostListView(ListAPIView):
    serializer_class = PostStreamSerializer
    def get_queryset(self):
        user = self.request.user
        posts = Stream.objects.filter(user=user)
        group_ids = []
        for post in posts:
            group_ids.append(post.post.id)
        qs = Post.objects.all().filter(id__in=group_ids).order_by('-posted')
        return qs








































# from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView
# from .models import Stream, Post
# from rest_framework.response import Response
# from rest_framework import permissions
# from .serializers import *
# from itertools import chain

# class HomePageStream(ListCreateAPIView):
#     serializer_class = StreamSerializer

#     def get_queryset(self):
#         user = self.request.user
#         qs = Stream.objects.filter(user=user)
#         return qs


    
    
