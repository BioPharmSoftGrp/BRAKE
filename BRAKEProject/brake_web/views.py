from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required
from BRAKE.forms import RPackForm
from brake_secure.models import RPack

# Create your views here.
def home( request ):
    return render(request, 'brake_web/home.html', {'currentPage':'home'})

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
            return( redirect( 'home') )

def logoutuser(request):
    if request.method == "POST":
        logout( request )
        return redirect( 'home' )

def CurrentPackages(request):
    # TODO: sanitize query
    query = request.GET.get('search', None)

    # Super basic search. Splits the query string into words and
    # only includes packages that have at least one of those words
    # in its name, description, author, or maintainer. Case insensitive.
    packages = RPack.objects.all() if query in [[], '', None] else \
        [pack for pack in RPack.objects.all() if
         any(word.lower() in pack.name.lower()
             or word.lower() in pack.description.lower()
             or word.lower() in pack.author.lower()
             or word.lower() in pack.maintainer.lower()
             for word in query.split())]
    
    return render(request, 'brake_web/CurrentPackages.html',
                  {'currentPage':'CurrentPackages','packages':packages, 'searchQuery':query})


def ViewPackage(request, RPack_pk):
    #TODO: WE allow users to view all pacakges but only allow them to update if they are looged in AND own the project
    package = get_object_or_404( RPack, pk = RPack_pk )
    if request.method == "GET":
        form = RPackForm(instance = package)
        return render( request, 'brake_web/ViewPackage.html',
                       {'currentPage':'ViewPackage','package':package, 'form':form})
    else:
        try:
            form = RPackForm( request.POST, instance=package )
            form.save()
            return redirect( 'CurrentPackages' )
        except ValueError:
            return render( request,  'brake_web/ViewPackage.html',
                           {'currentPage':'ViewPackage', 'package':package,
                            'form':form, 'error':'Bad data passed in'})

def AddNewPackage(request):
    if request.method == "GET":
        return render( request, 'brake_web/AddNewPackage.html',
                       {'currentPage':'AddNewPackage','form':RPackForm()})
    else:
        # User is posting to add a new prackage
        try:

            user = request.user
            bBpsuser = False
            if not user.is_authenticated:
                #TODO: BAD PRACTICE TO USE USER NAME AND PASSWORD RIGHT HERE BUT CHECING THE IDEA
                user = authenticate( request, username = 'bpsuser.20' , password = 'get.Smart_20')
                bBpsuser = True
                login(request, user)

            form = RPackForm( request.POST )
            newRPack = form.save( commit = False )
            newRPack.user = user
            newRPack.save()

            if bBpsuser:
                logout( request )

            return redirect( 'home' )  #TODO: This should go back to the list of packages.
        except ValueError:
            return render( request, 'brake_web/AddNewPackage.html' ,
                           {'currentPage':'AddNewPackage', 'form':RPackForm(),
                            'error':'Bad data passed in'})
