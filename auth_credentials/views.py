from django.http import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib.auth.models import User
from auth_credentials.models import Users
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def loginuser(request):
    if request.user.is_authenticated == True :
        return redirect('/')
    if (request.method == 'POST'):
        u_user = request.POST.get('u_user', '')
        u_password = request.POST.get('u_password', '')
        if (len(u_user) > 3 and len(u_password) > 4):
            user = authenticate(username=u_user, password=u_password)
            if(user is not None):
                login(request,user)
                messages.success(request,"You are logged in now")
                return redirect("/")
            else:
                messages.error(request,"Invalid crenditials")
                render(request, 'auth_cred/login.html')
        else:
            messages.error(request,"Invalid crenditials")
            render(request, 'auth_cred/login.html')
    return render(request, 'auth_cred/login.html')


def signupuser(request):
    if request.user.is_authenticated == True :
        return redirect('/')
    name = request.POST.get('name',"")
    email = request.POST.get('email',"")
    password = request.POST.get('password',"")
    if(request.method == "POST"):
        if(len(name) > 2 and len(email) > 5 and len(password) > 5):
            em = User.objects.filter(email=email)
            usr = User.objects.filter(username=name)
            if(len(usr) == 0 and len(em) == 0):
                user = User.objects.create_user(username=name,email=email,password=password)
                user.save()
                auth_user = Users(user_name=user,user_email=email)
                auth_user.save()
                messages.success(request, " Your Account has been successfully created")
                return render(request, 'auth_cred/signup.html')
            else:
               messages.error(request, "username or email will be taken")
               return render(request, 'auth_cred/signup.html')
        else:
            messages.error(request, "Enter a minimum 3 character for username and password")
            return render(request, 'auth_cred/signup.html')
    return render(request, 'auth_cred/signup.html')

def forgotuser(request):
    if request.user.is_authenticated == True :
        return redirect("/")
    if (request.method == 'POST'):
        email = request.POST.get('u_email','')
        password = request.POST.get('password','')
        user = User.objects.filter(email=email)
        if(user is not None):
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            messages.success(request,"Password has been successfully updated")
            return render(request, 'auth_cred/forgot.html')
        else:
            messages.success(request,"Invalid creanditials")
            return render(request, 'auth_cred/forgot.html')
    return render(request, 'auth_cred/forgot.html')

@login_required
def logoutuser(request):
    if request.user.is_authenticated == False :
        return redirect("/")
    logout(request)
    return redirect("/")

@login_required
def userdeshboard(request,uname):
    if request.user.is_authenticated == False :
        return redirect('/')
    user = request.user
    usr = Users.objects.filter(user_name=user)
    params = {'ud':""}
    for ur in usr:
        params = {'ud':ur}
    return render(request,"auth_cred/dashboard.html",params)

@login_required
def editprofile(requet,uname):
    user = requet.user
    if(requet.user.is_authenticated == False):
        return redirect("/")
    if(requet.method == "POST"):
        fname = requet.POST.get("f_name","")
        lname = requet.POST.get("l_name","")
        address = requet.POST.get("address","")
        about = requet.POST.get("about","")
        gender = requet.POST.get("gender","")
        phone = requet.POST.get("phone","")
        img = requet.FILES.get("img","Images/auser.png")
        u = Users.objects.filter(user_name=user).update(user_first_name=fname,user_last_name=lname,gender = gender,contact_no = phone,address = address,about_user = about,user_image=img)
        
        return redirect(f"/authcreadentials/dashboard/@{user.username}/")
    ur = Users.objects.filter(user_name=user)
    for i in ur:
        ur = i
    print(ur.about_user)
    params = {'uinfo':ur}
    return render(requet,'auth_cred/edit_profile.html',params)