from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, FormView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests import request

from .models import Follow, Profile
from common.decorators import ajax_required
from activity.utils import create_activity
from .forms import EditProfileForm
# Create your views here.


class FollowerListView(ListView):
    # model = Follower
    context_object_name = "followers"
    template_name = "followers/followers_list.html"

    def get_queryset(self):
        self.queryset = self.request.user.followers.all()
        return super().get_queryset()


class FollowingListView(ListView):
    # model = Follower
    context_object_name = "following"
    template_name = "followers/following_list.html"

    def get_queryset(self):
        self.queryset = self.request.user.following.all()
        return super().get_queryset()


class UserProfileView(SingleObjectMixin, FormView):
    model = Profile
    context_object_name = "user_profile"
    template_name = "followers/user_profile.html"
    form_class = EditProfileForm
    success_url = "."

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context["user_whispers"] = self.get_object().user.whispers.all()
        return context

    def get_initial(self):
        return {"user": self.request.user}

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            user_profile = self.get_object()
            user_profile.avatar = form.cleaned_data["avatar"]
            user_profile.save()
            messages.success(self.request, "Profile updated successfully")
        except Exception as e:
            print(e)
            messages.error(self.request, "Unable to update profile")
        return super().form_valid(form)


class FollowUserView(View):
    def post(self, request, *args, **kwargs):
        user_model = get_user_model()
        user_to = get_object_or_404(user_model, id=request.POST.get("user_to"))

        if user_to.id == request.user.id:
            return JsonResponse({"message": "error"})

        try:
            follow = Follow.objects.get(
                user_from=request.user, user_to=user_to)
            follow.delete()
            create_activity(
                request.user, f'unfollows {user_to.username}', user_to)
            return JsonResponse({"message": "info"})
        except Follow.DoesNotExist:
            Follow.objects.create(user_from=request.user, user_to=user_to)
            create_activity(
                request.user, f'follows {user_to.username}', user_to)
            return JsonResponse({"message": "success"})
        except IntegrityError:
            return JsonResponse({"message": "error"})
