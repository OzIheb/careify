from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html',context={'counter':User.getcounter()})

def login(request):
    return render(request, 'login.html')

def landing(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        #get the post parameters
        username = first_name+str(User.getcounter())
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        user = User(username=username, first_name=first_name, last_name=last_name, password=password, phone_number=phone_number, address=address, city=city, state=state)
        user.save()
        return redirect(request, 'login.html')

def authentification(request):
    if request.method == 'POST':
        #get the post parameters
        login_username = request.POST['username']
        login_password = request.POST['password']
        try:
            user = User.objects.get(username=login_username)
        except:
            user = None
        if user is not None and user.password == login_password:
            return redirect(request, 'landing.html')    
        else:
            return redirect(request, 'login.html')






# Create your views here.