from django.conf.urls import url,include
from django.urls import path
from . import views
# from .forms import StudentLoginForm
from django.contrib.auth.views import *
    #LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

app_name = 'online_books'

urlpatterns = [

    # path('', LoginView.as_view(template_name='stud_app/login.html',authentication_form=StudentLoginForm), name="login"),
    # url('login/',  views.StudentView.as_view(), name="login"),

    # path('', views.blank_page),
    # path('login/', views.login_view, name="login"),
    path('login/',  login, name="login"),
    path('logout/', LogoutView.as_view(template_name='online_books/logout.html'), name="logout"),
    # path('<username>/home/', views.home_view, name="home"),
    # path('<username>/courses/', views.courses_view, name="courses"),
    # path('<username>/exams/', views.exam_list_view, name="exams"),
    # path('<username>/exams/<int:exam_id>', views.exam_view, name="exams"),
    # path('<username>/scores/', views.scores_view, name="scores"),

]