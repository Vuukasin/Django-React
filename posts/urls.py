from django.urls import path
from .views import *

urlpatterns = [

    # path('api/home/stream/', HomePageStream.as_view()),
    path('api/post-stream/', PostListView.as_view()),

]