from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from BRAKE.forms import RPackForm
from brake_secure.models import RPack

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

def CurrentPackages(request):
    packages = RPack.objects.all()
    return render( request, 'brake_web/CurrentPackages.html', {'packages':packages})


def ViewPackage(request, RPack_pk):
    #TODO: WE allow users to view all pacakges but only allow them to update if they are looged in AND own the project
    package = get_object_or_404( RPack, pk = RPack_pk )
    if request.method == "GET":
        form = RPackForm(instance = package)
        return render( request, 'brake_web/ViewPackage.html', {'package':package, 'form':form})
    else:
        try:
            form = RPackForm( request.POST, instance=package )
            form.save()
            return redirect( 'CurrentPackages' )
        except ValueError:
            return render( request,  'brake_web/ViewPackage.html', {'package':package, 'form':form, 'error':'Bad data passed in'})

def AddNewPackage(request):
    if request.method == "GET":
        return render( request, 'brake_web/AddNewPackage.html' , {'form':RPackForm()})
    else:
        # User is posting to add a new prackage
        try:
            form = RPackForm( request.POST )
            newRPack = form.save( commit = False )
            newRPack.user = request.user
            newRPack.save()
            return redirect( 'home' )  #TODO: This should go back to the list of packages.
        except ValueError:
            return render( request, 'brake_web/AddNewPackage.html' , {'form':RPackForm(), 'error':'Bad data passed in'})
