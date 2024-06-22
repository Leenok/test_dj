from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect



def index_logout (request) :
    if request.method == "POST" :
        logout(request)
        return redirect(auth)
    else:
        return render(request,"TimurIndex.html")    




            
        


