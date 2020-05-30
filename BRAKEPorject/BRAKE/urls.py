"""BRAKE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# brake_web - contains the pages that the public sees and can access
from brake_web import views as brake_web_views

# brake_secure - contains the pages that only a user can access once logged in
#from brake_secure import views as brake_secure_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # break_web urls
    # Authentication
    path('signup/', brake_web_views.signupuser, name ='signupuser'),
    path('logout/', brake_web_views.logoutuser, name ='logoutuser'),
    path('login/', brake_web_views.loginuser, name ='loginuser'),

    # Public
    path( '', brake_web_views.home, name='home'),
    path( 'CurrentPackages/', brake_web_views.currentRPackages, name='CurrentPackages'),
    path( 'addpackage/', brake_web_views.addpackage, name='addpackage'),
    path( 'package/<int:RPack_pk>', brake_web_views.ViewPackage, name='ViewPackage'),

    # brake_secure urls
    #path('secure/', brake_secure_views.securehome, name ='securehome'),
    path( 'secure/', include( 'brake_secure.urls'))
]

#urlpatterns += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
