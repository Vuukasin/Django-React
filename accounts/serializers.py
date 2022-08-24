# from pyexpat import model
# from .models import *
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from posts.models import *
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'


# class HomeProfileSerializer(serializers.ModelSerializer):
#     following_count = serializers.SerializerMethodField('_get_following_count')
#     followers_count = serializers.SerializerMethodField('_get_followers_count')
#     post_count = serializers.SerializerMethodField('_get_post_count')
#     username = serializers.SerializerMethodField('_get_username')
#     first_name = serializers.SerializerMethodField('_get_first_name')
#     last_name = serializers.SerializerMethodField('_get_last_name')
#     notification_count = serializers.SerializerMethodField('_get_notification_count')

#     def _get_following_count(self, profile_object):
#         following_count = Follow.objects.all().filter(follower=profile_object.user).count()
#         return following_count

#     def _get_followers_count(self, profile_object):
#         followers_count = Follow.objects.all().filter(following=profile_object.user).count()
#         return followers_count

#     def _get_post_count(self, profile_object):
#         post_count = Post.objects.all().filter(user=profile_object.user).count()
#         return post_count

#     def _get_notification_count(self, profile_object):
#         notification_count = Notification.objects.filter(user=profile_object.user).count()
#         return notification_count

#     def _get_username(self, profile_object):
#         return profile_object.user.username
    
#     def _get_first_name(self, profile_object):
#         return profile_object.user.first_name
    
#     def _get_last_name(self, profile_object):
#         return profile_object.user.last_name

#     class Meta:
#         model = Profile
#         fields = ['avatar', 'following_count', 'followers_count', 'post_count', 'username', 'first_name', 'last_name', 'notification_count']


# class AvatarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['avatar']


# class HomeProfileSerializer(serializers.ModelSerializer):
#     following_count = serializers.SerializerMethodField('_get_following_count')
#     followers_count = serializers.SerializerMethodField('_get_followers_count')
#     post_count = serializers.SerializerMethodField('_get_post_count')
#     first_name = serializers.SerializerMethodField('_get_first_name')
#     last_name = serializers.SerializerMethodField('_get_last_name')
#     notification_count = serializers.SerializerMethodField('_get_notification_count')

#     def _get_following_count(self, user_object):
#         following_count = Follow.objects.all().filter(follower=user_object).count()
#         return following_count

#     # def _get_avatar(self, user_object):
#     #     return user_object.profile.avatar

#     def _get_followers_count(self, user_object):
#         followers_count = Follow.objects.all().filter(following=user_object).count()
#         return followers_count

#     def _get_post_count(self, user_object):
#         post_count = Post.objects.all().filter(user=user_object).count()
#         return post_count

#     def _get_notification_count(self, user_object):
#         notification_count = Notification.objects.filter(user=user_object).count()
#         return notification_count

    
#     def _get_first_name(self, user_object):
#         return user_object.first_name
    
#     def _get_last_name(self, user_object):
#         return user_object.last_name

#     class Meta:
#         model = User
#         fields = ['following_count', 'followers_count', 'post_count', 'username', 'first_name', 'last_name', 'notification_count', 'avatar']

