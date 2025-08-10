from django.urls import path

from user.views import RegisterView, LoginView, ConfirmEmailView, LogoutView, UserProfileView

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('confirmation/<int:uid>/<str:token>', ConfirmEmailView.as_view(), name='confirmation'),
]