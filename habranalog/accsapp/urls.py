
from django.urls import path
from accsapp.views import *
from . import views
app_name = 'accsapp'
urlpatterns=[
    path('sign-up/',signup, name='signup' ),
    path('sign-in/',signin, name='signin' ),
    path('sign-out/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path('rename/', change_username, name ='rename'),
    path('change_username/', views.change_username, name='change_username')


]