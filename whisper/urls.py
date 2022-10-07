from django.urls import path

from .views import LikeWhisperView, WhisperCreateView, WhisperListView

app_name = "whisper"

urlpatterns = [
    path("", WhisperListView.as_view(), name="whisper_list"),
    path("new-whisper/", WhisperCreateView.as_view(), name="whisper_create"),
    path("like/<int:pk>/", LikeWhisperView.as_view(), name="like_whisper"),
]
