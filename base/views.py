from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'home.html')

class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'base/register.html', {'rF':rF})
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('save user success')
    

class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'base/login.html', {'lF': lF})
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            return HttpResponse('login fail')
        
def logoutUser(request):
    logout(request)