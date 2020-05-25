from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home( request ):
    return render( request, 'brake_web/home.html')

def signupuser(request):
    if request.method == "GET":
        return render( request, 'brake_web/signupuser.html' , {'form':UserCreationForm()})
    else:
        # Create a new User
        if( request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user( request.POST['username'], password=request.POST['password1'] )
                user.save()
                login(request, user)
                return( redirect( '../secure') )
            except IntegrityError:
                return render( request, 'brake_web/signupuser.html', {'form':UserCreationForm(), 'error':'User name has already been created, please choose another user name and try again.'})
        else:
            return render( request, 'brake_web/signupuser.html', {'form':UserCreationForm(), 'error':'Password did not match, please try again.'})

def loginuser(request):
    if request.method == "GET":
        return render( request, 'brake_web/loginuser.html' , {'form':AuthenticationForm()})
    else:
        user = authenticate( request, username = request.POST['username'] , password = request.POST['password'])
        if user is None:
            return render( request, 'brake_web/loginuser.html' , {'form':AuthenticationForm(), 'error':'Username and password did not match.'})
        else:
            login(request, user)
            return( redirect( '../secure') )

def logoutuser(request):
    if request.method == "POST":
        logout( request )
        return redirect( 'home' )
