from django.urls import path
from . import views
from django.shortcuts import render


app_name = 'account'

urlpatterns = [
    # Registration and verification
    path('register/',views.register_user,name='register'),
    path('email-verification-sent/',
         lambda request:render(
             request, 'account/email/email-verification-sent.html'),
         name='email-verification-sent'
         ),
    #Login & Logout
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

    #dashboard
    path('dashboard/',views.dashboard_user,name='dashboard'),
    path('profile-management/',views.profile_user,name='profile-management'),
    path('account-delete/',views.delete_user,name='account-delete'),
]



