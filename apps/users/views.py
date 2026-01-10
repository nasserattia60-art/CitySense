from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.



from django.contrib.auth.models import User

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:home")
        else:
            if "username" in form.errors or "email" in form.errors:
                return redirect("users:login")
    return render(request, "users/register.html", {"form": form})





@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    

    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )
    if form.is_valid():
        form.save()

    context = {
        "form": form,
        "user": request.user,
        "profile": profile,
    }
    return render(request, "users/profile.html", {"form": form, "context": context})
