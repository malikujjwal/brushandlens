from django.urls import path

from .views import (
    LogInView, SignUpView, LogOutView, ChangeProfileView, ChangePasswordView,
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
]
