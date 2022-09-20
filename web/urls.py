from django.urls import path
from . import views

app_name='web'

urlpatterns =[

    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('forgot-password/',views.forgot_password,name='forgot_password'),
    path('profile/',views.profile,name='profile'),
    path('settings/',views.settings,name='settings'),
    path('dashboard/',views.index,name='index')
]