from django.conf.urls import url,include
from django.urls import path
from . import views
from django.contrib.auth.views import *
    #LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

app_name = 'online_books'

urlpatterns = [
    path('home/', views.home_view, name='home'),

]