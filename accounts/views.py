from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import AuthorizationKey


def signup(request):
    if request.method == 'POST':
        if request.POST['authorization_key']:
            if AuthorizationKey.objects.filter(key=request.POST['authorization_key']).count() is not 0:
                if request.POST['password'] == request.POST['password2']:
                    if  User.objects.filter(username=request.POST['username']).count() is not 0:
                        return render(request, 'accounts/signup.html', {'error' : 'Username is taken'})
                    else:
                        user = User.objects.create_user(request.POST['username'], 
                                                        request.POST['email'], request.POST['password'])
                        auth.login(request, user)
                        return redirect('all_articles')
                else:
                    return render(request, 'accounts/signup.html', {'error' : 'Passwords do not match'})
            else:
                return render(request, 'accounts/signup.html', {'error' : 'Contact administrator for valid authorization key'})
        else:
            return render(request, 'accounts/signup.html', {'error' : 'No authorization key provided'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        if request.POST['password'] and request.POST['username']:
            if  User.objects.filter(username=request.POST['username']).count() is 0:
                return render(request, 'accounts/login.html', {'error' : 'User does not exist'})
            else:
                user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    auth.login(request, user)
                    return redirect('all_articles')
                else:
                    return render(request, 'accounts/login.html', {'error' : 'Incorrect Credentials'})
        else:
            return render(request, 'accounts/login.html', {'error' : 'User does not exist'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')