from django.urls import path
from . import views

#Specifying the name of the app is a good practice.
# By specifying the blog name we now we can used it when we refernce
# pages in this app.  See the all_blogs.html where it references
# the description page using the name blog from here.
# If we did not do this and there was another detail.html, say in the protfolio
# then Djago would grab the first one and may not be correct

app_name = 'brake_secure'

urlpatterns = [
    path('', views.securehome, name='securehome'),
    #path('<int:blog_id>/', views.detail, name='detail'),
]
