from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.core.files.images import get_image_dimensions
from notifications.models import Notification
from django.db.models.signals import post_delete, post_save
User = get_user_model()


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'#{self.name}'


class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path)
    text = models.TextField(max_length=255, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(HashTag, blank=True)
    image_size = models.FloatField(default=1)


    def save(self, *args, **kwargs):
        w, h = get_image_dimensions(self.image)
        self.image_size = w / h
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=False)


    def __str__(self):
        return f'{self.user.username} - Comment'

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.follower.username} -> {self.following.username}'

    def user_follow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification(sender=sender, user=following, notification_type=3)
        notify.save()
    
    def user_unfollow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        following = follow.following
        notify = Notification.objects.filter(sender=sender, user=following, notification_type=3)
        notify.delete()

post_save.connect(Follow.user_follow, sender=Follow)
post_delete.connect(Follow.user_unfollow, sender=Follow)


class Stream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_profile')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stream_following')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def add_post(sender, instance, created, *args, **kwargs):
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
            stream.save()

    def add_following(sender, instance, created, *args, **kwargs):
        posts = Post.objects.all().filter(user=instance.following)
        if created:
            for post in posts:
                Stream.objects.create(post=post, following=instance.following, user=instance.follower)

    def __str__(self):
        return f'{self.user} -> {self.following}'


post_save.connect(Stream.add_post, sender=Post)
post_save.connect(Stream.add_following, sender=Follow)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['user', 'post'], name='unique_like')
    #     ]

    # @classmethod
    # def get_like_count(self, *args, **kwargs):
    #     return Like.objects.filter(post=self.post).count()

    def user_liked_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
        notify.save()


    def user_unlike_post(sender, instance, *args, **kwargs):
        like = instance
        post = like.post
        sender = like.user
        notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
        notify.delete()


post_delete.connect(Like.user_unlike_post, sender=Like)
post_save.connect(Like.user_liked_post, sender=Like)


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_owner')
    content = models.FileField(upload_to=user_directory_path)
    expired = models.BooleanField(default=False)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class StoryStream(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_following')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='stories')
    date = models.DateTimeField(auto_now_add=True)


    def add_followingg(sender, instance, created, *args, **kwargs):
        stories = Story.objects.all().filter(user=instance.following)
        if created:
            for story in stories:
                StoryStream.objects.create(following=instance.following, user=instance.follower, story=story, date=story.posted)


    def add_story(sender, instance, *args, **kwargs):
        new_story = instance
        user = new_story.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            storystream = StoryStream(story=new_story, user=follower.follower, date=new_story.posted, following=user)
            storystream.save()

    # def add_post(sender, instance, created, *args, **kwargs):
    #     post = instance
    #     user = post.user
    #     followers = Follow.objects.all().filter(following=user)
    #     for follower in followers:
    #         stream = Stream(post=post, user=follower.follower, date=post.posted, following=user)
    #         stream.save()

post_save.connect(StoryStream.add_story, sender=Story)
post_save.connect(StoryStream.add_followingg, sender=Follow)

