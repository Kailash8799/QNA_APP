
from django.urls import path,include
from . import views


urlpatterns = [
    path('login/', views.loginuser,name="login"),
    path('signup/', views.signupuser,name="signup"),
    path('forgot/', views.forgotuser,name="forgot"),
    path('logout/', views.logoutuser,name="logout"),
    path('dashboard/', views.userdeshboard,name="profile"),
]
