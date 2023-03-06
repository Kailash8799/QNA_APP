
from django.urls import path,include
from . import views


urlpatterns = [
    path('login/', views.loginuser,name="login"),
    path('signup/', views.signupuser,name="signup"),
    path('forgot/', views.forgotuser,name="forgot"),
    path('logout/', views.logoutuser,name="logout"),
    path('dashboard/@<uname>/', views.userdeshboard,name="profile"),
    path('dashboard/@<uname>/editprofile/', views.editprofile,name="edit_profile"),
]
