from django.urls import path
from django.contrib.auth import views  as auth_views
from my_app.views import upkeepp, UserLoginView, UserRegistrationView


urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('profile', upkeepp.UserProfileView.as_view(), name='profile'),
    path('SendResetPasswordEmail', upkeepp.SendPasswordResetEmailView.as_view(), name='SendResetPasswordEmail'),
    path('resetPassword/<uid>/<token>', upkeepp.UserPasswordResetView.as_view(), name = 'reset-Password'),

    path('oauth/login', upkeepp.SocialLoginView.as_view())

]
