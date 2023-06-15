from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from articleapp.models import *
from django.contrib import messages
from articleapp.forms import ChangeUserName

def signup(request):
    if request.user.is_authenticated:
        return redirect('articleapp:home')

    if request.method == 'GET':
        return render(request, 'accsapp/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('articleapp:home')

            except IntegrityError:
                return render(request, 'accsapp/signup.html', {'form': UserCreationForm(), 'error': 'такой пользователь уже существует'})

        else:
            return render(request, 'accsapp/signup.html', {'form': UserCreationForm(), 'error': 'пароли не совпадают'})
def signin(request):
    if request.user.is_authenticated:
        return redirect('articleapp:home')
    if request.method=='GET':
        return render(request, 'accsapp/signin.html', {'form':AuthenticationForm()})
    else:
        user=authenticate(request, username =request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'accsapp/signin.html',{'form':AuthenticationForm(),'error':'такого пользователя не существует'})
        else:
            login(request,user)
            return redirect('articleapp:home')

@login_required
def signout(request):
    logout(request)
    return redirect('articleapp:home')

@login_required
def profile(request):
    username = request.user.username
    publicart=Article.objects.filter(author=request.user, published=True)
    privateart = Article.objects.filter(author=request.user, published=False)
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    date_joined = request.user.date_joined.strftime('%Y-%m-%d')
    return render(request, 'accsapp/profile.html', context={'publicart' :publicart, 'privateart':privateart, 'username': username,
                                                            'first_name':first_name, 'last_name':last_name, 'email':email, 'date_joined':date_joined})

@login_required
def change_username(request):
    if request.method == 'POST':
        form = ChangeUserName(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Имя пользователя успешно изменено.')
            return redirect('accsapp:profile')
        else:
            messages.error(request, 'При изменении имени пользователя произошла ошибка.')
    else:
        form = ChangeUserName(instance=request.user)

    context = {'form': form}
    return render(request, 'accsapp/change_username.html', context=context)