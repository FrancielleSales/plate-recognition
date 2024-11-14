from django.urls import path
from users.views.login import UserLoginView
from users.views.register import UserRegisterView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
