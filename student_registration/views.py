from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import extendeduser
def home(request):
    return render(request,'student_registration/home.html')

def loginuser(request):
    if request.method == "GET":
        return render(request,'student_registration/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'student_registration/loginuser.html',{'form':AuthenticationForm(),'error':'Username & password does not exists'})
        else:
            login(request,user)
            return redirect('welcome')
def signupuser(request):
    if request.method == "GET":
        return render(request, 'student_registration/regiter.html')
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request,'student_registration/regiter.html',{'error':"UserName Has Already Been Taken"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                fullname=request.POST['fullname']
                profile = request.POST['profile']
                newextendeduser=extendeduser(fullname=fullname,profile=profile,user=user)
                newextendeduser.save()
                login(request,user)
                return redirect('welcome')
        else:
            return render(request,'student_registration/regiter.html',{'error':'password does not match'})

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

@login_required
def welcome(request):
        datas = extendeduser.objects.filter(user=request.user,profile="student")
        if datas:
            return render(request,'student_registration/student_wel.html',{'data':datas})
        else:
            return render(request,'student_registration/teacher_wel.html',{'data':datas})

