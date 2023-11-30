from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login



# Create your views here.
def home(request):
    return render(request,'home.html')

def signuppage(request):
    return render(request,'signuppage.html')

def loginform(request):
    return render(request,'loginform.html')

def welcomepage(request):
    return render(request,'welcomepage.html')

def add(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['user']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'the username already exist')
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password,email=email)
                user.save()
        else:
            messages.info(request,'password doesnot match')
            return redirect('signuppage')
        return redirect('loginform')
    else:
        return render(request,'signuppage.html')
    

def adminpage(request):
    return render(request,'adminpage.html')

def admin_log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('adminpage')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('welcomepage')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    return render(request,'signuppage.html')

def logout(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'aboutpage.html')