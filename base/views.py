from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User

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
        return render(request, 'home.html')
    def post(self, request):
        username = 'user_login'
        password = 'user_password'

        return HttpResponse(username)
        