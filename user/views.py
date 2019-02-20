from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import  RegistrationForm, UserForm, UserProfileForm, UserInfoForm
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



@login_required(login_url='/user/login/')
def myself(request):
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    return render(request, "user/myself.html", locals())


@login_required(login_url='/account/login/')
def myself_edit(request): 
    userprofile = UserProfile.objects.get(user=request.user) if hasattr(request.user, 'userprofile') else UserProfile.objects.create(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user) if hasattr(request.user, 'userinfo') else UserInfo.objects.create(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            request.user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            request.user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/user/my-information/')
    else: 
        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(instance=userprofile)
        userinfo_form = UserInfoForm(instance=userinfo)
        return render(request, "user/myself_edit.html", locals())




@login_required(login_url='/user/login/')
def my_image(request): 
    if request.method == 'POST':
        img = request.POST['img'] 
        userinfo = UserInfo.objects.get(user=request.user.id) 
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'user/imagecrop.html',)