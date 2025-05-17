from django.shortcuts import render
from .models import Posts
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def test(request):
    return render(request, 'blog/base.html')

def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request , user)
            return redirect('/home')
        else:
            return redirect('/loginn')
    
    return render(request, 'blog/loginn.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'blog/signup.html')

def home(request):
    context = {
        'posts':Posts.objects.all()
    }
    return render(request, 'blog/home.html' , context)