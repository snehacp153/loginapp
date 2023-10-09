from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # print(username,password)
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('home')
        messages.error(request,"please signup")
   
    return render(request,"login.html")
    
def index(request):
    return render(request,"index.html")

def logout(request):
    auth.logout(request)
    return render(request,"login.html")
