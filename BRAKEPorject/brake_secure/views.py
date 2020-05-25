from django.shortcuts import render, get_object_or_404

def securehome(request):
    #if request.method == "GET":
    return render( request, 'brake_secure/securehome.html' )
