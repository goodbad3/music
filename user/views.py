from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm,  UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo
from django.contrib.auth.models import User
from django.urls import reverse

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST) 
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False) 
            new_user.set_password(user_form.cleaned_data['password']) 
            new_user.save()
            new_profile = userprofile_form.save(commit=False) 
            new_profile.user = new_user
            new_profile.save()

            return HttpResponseRedirect(reverse("user:user_login"))

        else:
            return HttpResponse("注册信息填写失败，请重写注册！")
    else: 
        user_form = RegistrationForm() 
        userprofile_form = UserProfileForm()
        return render(request, "user/register.html", locals())