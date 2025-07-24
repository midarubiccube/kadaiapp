from django.urls import path
from django.contrib.auth import views as v
from .views import CustomLoginView, UserCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(next_page='/'), name='logout'),

    path('password_change/', v.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', v.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', v.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset///', v.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('create/', UserCreateView.as_view(), name="create"),
    #path('profile/', views.UserProfileView.as_view(), name="profile"),
    #path('change/', views.UserChangeView.as_view(), name="change"),
]