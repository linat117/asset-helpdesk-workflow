from django.urls import path
from .views import RegisterView, LoginView, CurrentUserView, logout_view, UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("user/",CurrentUserView.as_view(),name="current-user"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", logout_view, name="logout"), 
    path("admin/users/", UserListView.as_view(), name="user-list"),  

]
