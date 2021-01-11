from django.urls import path, include
from accounts.views import LogoutUserView, LoginUserView, RegisterView, user_profile

urlpatterns = [
    # path('',include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout_user/', LogoutUserView.as_view(), name='user logout'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('profile/',user_profile,name='user profile')

]