from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Confirm Pssword", widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'txt tabInput', 'placeholder':'数字/字母/特殊符号'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'txt tabInput', 'placeholder':'重复密码'})    
    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            'email': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder':'邮箱'}),
            'username': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder':'用户名'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("两个密码不一样！！！") 
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("phone", "birth")
        widgets = {
            'phone': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder':'1900/12/12'}),
            'birth': forms.widgets.TextInput(attrs={'class': 'txt tabInput', 'placeholder':'11位号码'}),
        }  


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", 'photo')


class UserForm(forms.ModelForm): 
    class Meta:
        model = User 
        fields = ("email",)      