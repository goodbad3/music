from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

app_name = "user"
urlpatterns = [ 
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),
    path('register2/', views.register, name='user_register2'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="user/password_change_form.html", success_url="/user/password-change-done/"), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset_form.html", email_template_name="user/password_reset_email.html", success_url='/user/password-reset-done/'), name='password_reset'),#视图函数也内置
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html", success_url='/user/password-reset-complete/'), name="password_reset_confirm"),#视图函数也内置
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
    path('my-information/', views.myself, name="my_information"),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    path('my-image/', views.my_image, name="my_image"),
  
]