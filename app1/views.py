from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse


# Create your views here.

def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(
            username=data["lgn"], password=data["psw"])
        if user is not None:
            request.session["is_auth"] = user.username
            # return redirect(index)
            return HttpResponse(f'Привет {user}')
        else:
            return HttpResponse(f"Неправильный пароль")
    else:
        return render(request, 'log_in.html')


def index(request):
    name = request.session.get("is_auth", "Не авторизован")
    if name != "Не авторизован":
        return render(request, 'index.html')
    else:
        return HttpResponse(f"Неправильный пароль")
