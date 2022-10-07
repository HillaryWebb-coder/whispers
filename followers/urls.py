from django.urls import path

from .views import FollowUserView, FollowerListView, UserProfileView, FollowingListView

app_name = "followers"

urlpatterns = [
    path("", FollowerListView.as_view(), name="followers_list"),
    path("<slug:slug>/", UserProfileView.as_view(), name="user_profile"),
    path("<slug:slug>/following/",
         FollowingListView.as_view(), name="following_list"),
    path("<slug:slug>/follow/", FollowUserView.as_view(), name="follow_user"),
]
