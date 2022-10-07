from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from .models import Like, Whisper
from .forms import WhisperForm
from activity.utils import create_activity
from activity.models import Activity


class WhisperListView(ListView):
    model = Whisper
    context_object_name = "whispers"
    template_name = "whispers/whisper_list.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all activities by default
        if self.request.user.is_authenticated:
            all_activity = Activity.objects.exclude(user=self.request.user)
            # Get all users followed by current user
            following_ids = self.request.user.following.values_list(
                "id", flat=True)
            if following_ids:
                all_activity = all_activity.filter(user_id__in=following_ids)
        else:
            all_activity = Activity.objects.all()
        context["activity"] = all_activity.select_related(
            'user', 'user__profile').prefetch_related('target')[:10]
        return context


class WhisperCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Whisper
    form_class = WhisperForm
    template_name = "whispers/whisper_create.html"
    success_url = reverse_lazy("whisper:whisper_list")
    success_message = "Whisper created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        create_activity(self.request.user, "created a new whisper")
        return super().form_valid(form)


class LikeWhisperView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            whisper = get_object_or_404(
                Whisper, id=request.POST.get("whisper_id"))
            Like.objects.update_or_create(
                user=request.user, whisper=whisper, liked=bool(request.POST.get("liked")), defaults={"liked": request.POST.get("liked")})
            create_activity(request.user, ("likes" if bool(
                request.POST.get("liked")) else "dislikes") + " " + str(whisper), whisper)
            return JsonResponse({"message": "success"})
        except IntegrityError:
            return JsonResponse({"message": "error"})
