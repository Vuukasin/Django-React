# from pyexpat import model
# from rest_framework import serializers
# from .models import *
# from accounts.serializers import *

from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class PostStreamSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_get_username')
    avatar_url = serializers.SerializerMethodField()
    like_count  = serializers.SerializerMethodField('_get_like_count')
    comment_count = serializers.SerializerMethodField('_get_comment_count')

    def _get_like_count(self, post_object):
        like_count = Like.objects.all().filter(post=post_object).count()
        return like_count

    def _get_comment_count(self, post_object):
        comment_count = Comment.objects.all().filter(post=post_object).count()
        return comment_count

    def _get_username(self, post_object):
        username = post_object.user.username
        return username

    class Meta:
        model = Post
        fields = ['uuid', 'image', 'username', 'avatar_url', 'like_count', 'comment_count', 'image_size']

    def get_avatar_url(self, post):
        request = self.context.get('request')
        avatar_url = post.user.profile.avatar.url
        return request.build_absolute_uri(avatar_url)



# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'

# class UserProfileSerializer(serializers.ModelSerializer):
#     profile = AvatarSerializer()
#     class Meta:
#         model = User
#         fields = ['profile']

# class PostStreamSerializer(serializers.ModelSerializer):
#     like_count = serializers.SerializerMethodField('_get_like_count')
#     comment_count = serializers.SerializerMethodField('_get_comment_count')
#     username = serializers.SerializerMethodField('_get_username')
#     user = UserProfileSerializer()

#     def _get_like_count(self, post_object):
#         return Like.objects.all().filter(post=post_object).count()

#     def _get_comment_count(self, post_object):
#         return Comment.objects.all().filter(post=post_object).count()

#     def _get_username(self, post_object):
#         return post_object.user.username

#     # def _get_profile(self, post_object):
#     #     return post_object.user.profile
    
#     class Meta:
#         model = Post
#         fields = ['uuid', 'image', 'like_count', 'comment_count', 'user', 'username']

# class StreamSerializer(serializers.ModelSerializer):
#     post = PostSerializer()
#     class Meta:
#         model = Stream
#         fields = ['id', 'post']