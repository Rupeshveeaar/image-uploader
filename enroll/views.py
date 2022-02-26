from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm ,Webs ,Webss, ImageForm
from django.contrib import messages
from .models import Image
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
# Create your views here.

"""Home Page"""
def Home_Page(request):
  if request.user.is_authenticated: # True
      if request.method == 'POST':
          fm= ImageForm(request.POST , request.FILES)
          if fm.is_valid():
            fm.save()
            messages.info(request, ' Image Successfully Upload!!')
            return HttpResponseRedirect('/home/')
      fm= ImageForm()
      img = Image.objects.all()   

      return  render (request, 'enroll/home.html',{'name':request.user, 'fm':fm , 'img':img})
  else:
     return HttpResponseRedirect('/')

"""Signup Page"""

def Sign_Page(request):
  if not request.user.is_authenticated: # True
       if request.method=='POST':
          fm=StudentForm(request.POST)
          if fm.is_valid():
            fm.save()
            fm=StudentForm()
            messages.info(request,"Create An Account  Successfuly!!")
            return HttpResponseRedirect('/home/')
       else:
         fm=StudentForm()
       return  render (request, 'enroll/sign.html',{'form':fm})
  else:
    return HttpResponseRedirect('/home/')


"""Login Page"""

def Login_Page(request):
    if not request.user.is_authenticated:  #True
      if request.method=='POST':
            fm=AuthenticationForm(request=request,  data=request.POST)
            if fm.is_valid():
                name=fm.cleaned_data['username']
                passw=fm.cleaned_data['password']
                user=authenticate(username=name , password=passw)
                if user is not None:
                    login(request, user)
                    messages.info(request, "login  Successfuly!!!")
                    return HttpResponseRedirect('/') # ye chalega
      else:
        fm=AuthenticationForm()
      return  render (request, 'enroll/login.html',{'form':fm})
    else:
        return  HttpResponseRedirect('/home/')

"""Logout Page"""

def Logout_Page(request):
    logout(request)
    messages.info(request ,"Logout Successfully!!")
    return HttpResponseRedirect ('/login/')




"""ChangePasswordForm with old Password Page"""


def ChangePaas(request):
  if  request.user.is_authenticated:
    if request.method=='POST':
        fm=Webs(user=request.user ,data=request.POST,)
        if fm.is_valid():
          fm.save()
          messages.info(request, "Password changed Successfully!!!")
          return HttpResponseRedirect('/login/')
    else:
        fm=Webs(user=request.user)     
    return render(request, 'enroll/changepass.html',{'form':fm}) 
  else:
     return HttpResponseRedirect('/login/')


"""Setpasssword Page"""

def Set_pass_Form(request):
  if request.user.is_authenticated:
      if request.method=='POST':
              fm=Webss(user=request.user ,data=request.POST)
              if fm.is_valid():
                fm.save() 
                update_session_auth_hash(request, fm.user) #function hai
                messages.info(request, " Password Set successfully!!!")
                return HttpResponseRedirect('/home/')
      else:
        fm=Webss(user=request.user)    
      return render(request, "enroll/setpass.html",{'form':fm})
  else:
    return HttpResponseRedirect('/login/')


