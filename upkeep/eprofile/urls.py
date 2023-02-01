from django.urls import path,include
from django.contrib.auth import views  as auth_views
from eprofile.views import UserChangePasswordView, UserEditUsernameEmailView,UserEditImageView


urlpatterns = [

    path('changepassword', UserChangePasswordView.as_view(), name='changepassword'),
    path('changeUsername&Email',UserEditUsernameEmailView.as_view(), name='changeusername-changeemail'),
    path('changeimage',UserEditImageView.as_view(),name='changeimage')
    
    
]
