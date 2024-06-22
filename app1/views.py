from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request, 'index.html')

def reg(request):
    # res = User.objects.all()
    if request.method == "POST":
        not_valid = ''
        data = request.POST
        user = User.objects.create_user(data['login'],data['email'],data['password'])
        user.first_name = data['name']

        if data['password'] == data['password2']:
            user.save()
            auth(request)
            return redirect(index)
        
        else:
            not_valid = 'Неверный пароль'
            return render(request, 'reg.html',  {'not_valid_regist': not_valid})
        
    else:
        return render(request, 'reg.html')
    

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username = data['login'], password = data['password'])
        if user is not None:
            request.session['is_auth'] = user.username
            return redirect(index)
        else:
            return render(request, 'auth.html')
    else:
        return render(request, 'auth.html')
