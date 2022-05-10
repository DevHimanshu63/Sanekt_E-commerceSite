from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from SubApp.models import Contact
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home/home.html')



def handlesignup(request):
    # if request.method=='POST':
    if request.method =="POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.Last_name=lname
        myuser.save()
        messages.success(request,"your account is created successfull!")
        return redirect("/signup")

    else:
        # messages.error(request,'Enter valid credential')
        # return HttpResponse('not found')
    
        return render(request,'home/signup.html')



# login page handle here
def handlelogin(request):
    if request.method=="POST":
        loginusername= request.POST["loginusername"]
        loginpass= request.POST["loginpass"]
        user= authenticate(username=loginusername,password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,"successfully loggedin")
            return redirect("/login")
        else:
            messages.error(request,"invalid credential!")
            return redirect("/login")
    return render(request,'home/login.html')



def handlelogout(request):
    logout(request)
    return redirect('/home')
    



def contact(request):
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['email']
        subject=request.POST['subject']
        desc=request.POST['desc']
        if len(name)<2  or len(subject)<5:
            return HttpResponse("Please fill name and subject correctly")
        else:
            obj=Contact(name=name,email=email,subject=subject,desc=desc)
            obj.save()
            redirect('/contact')
            messages.success(request,"Your Message has been sent successfully!")
    return render(request,'home/contact.html')

