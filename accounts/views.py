# from django.shortcuts import render
# from rest_framework.response import Response
# from django.http import JsonResponse
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
# from .serializers import *
# from django.contrib.auth import get_user_model
# from .models import Profile
# from rest_framework.decorators import api_view
# User = get_user_model()
# from rest_framework import status
# from django.db.models import Count

# class UserListView(ListCreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_url_kwarg = 'username'


# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = 'username'


# class HomePageProfile(ListCreateAPIView):
#     serializer_class = HomeProfileSerializer
#     def get_queryset(self):
#         user = self.request.user
#         return Profile.objects.filter(user=user)


# @api_view(['GET'])
# def profile_stats(request):
#     user = request.user
#     profile = Profile.objects.filter(user=user)
#     return Response({'message': 'Success', 'avatar': ProfileAvatarSerializer(profile, many=True).data}, status=status.HTTP_200_OK)