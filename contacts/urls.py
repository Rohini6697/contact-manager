from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.register,name='signup'),
    path('login/',views.signin,name='login'),
    path('dashboard/',views.dashboard,name='admindashboard'),
    path('home/',views.home,name='home'),
    path('addcontact/',views.addcontact,name='addcontact'),
    path('add_new_contact/',views.add_new_contact,name='add_new_contact'),
    path('delete_contact/<int:id>/',views.delete_contact,name='delete_contact'),
    path('updatecontact/<int:id>/',views.update_contact,name='update_contact'),
    path('contactlist/',views.contactlist,name='contactlist'),
    path('userslist/',views.userslist,name='userslist'),
    path('profile/',views.profile,name='profile'),
    path('delete_userlist/<int:id>',views.delete_user,name='delete_user')
]



