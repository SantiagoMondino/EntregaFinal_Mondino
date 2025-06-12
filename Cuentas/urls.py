from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (
    CustomLoginView, 
    CustomLogoutView, 
    SignUpView,
    ProfileView, 
    ProfileUpdateView, 
    CustomPasswordChangeView
)

urlpatterns = [
    path(_('login/'), CustomLoginView.as_view(), name='login'),
    path(_('logout/'), CustomLogoutView.as_view(), name='logout'),
    path(_('signup/'), SignUpView.as_view(), name='signup'),
    path(_('profile/'), ProfileView.as_view(), name='profile'),
    path(_('profile/update/'), ProfileUpdateView.as_view(), name='profile_update'),
    path(_('profile/change-password/'), 
         CustomPasswordChangeView.as_view(), 
         name='password_change'),
]