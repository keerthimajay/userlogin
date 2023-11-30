from .import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('loginform',views.loginform,name='loginform'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('add',views.add,name='add'),
    path('admin_log',views.admin_log,name='admin_log'),
    path('welcomepage',views.welcomepage,name='welcomepage'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('logout',views.logout,name='logout'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
]