from django.urls import path
from . import views

urlpatterns = [
    # path('', views.test),
    path('loginn/', views.loginn),
    path('', views.signup),
    path('home/', views.home),
    path('newpost/', views.newpost),
    path('mypost/', views.mypost),
    path('signout/', views.signOut),
]