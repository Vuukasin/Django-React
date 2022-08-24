from django.contrib import admin
from .models import Post, Story, StoryStream, Comment, Like, Stream, HashTag, Follow

admin.site.register(Post)
admin.site.register(Story)
admin.site.register(StoryStream)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Stream)
admin.site.register(HashTag)
admin.site.register(Follow)