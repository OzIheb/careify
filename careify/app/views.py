from django.shortcuts import render, redirect
from .models import customer

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def landing(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        #get the post parameters
        username = request.POST['username'] 
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        password = request.POST['password']
        phone_number = request.POST['phonenumber']
        address = request.POST['street-address']
        city = request.POST['city']
        state = request.POST['region']
        postal_code = request.POST['postal-code']
        try:
            
            user = customer(username=username,postal_code=postal_code, first_name=first_name, last_name=last_name, password=password, phone_number=phone_number, address=address, city=city, state=state)
            user.save()
        except:
            return redirect( '/signup/')
        return redirect( '/login/')

def authentification(request):
    if request.method == 'POST':
        #get the post parameters
        login_username = request.POST['username']
        login_password = request.POST['password']
        try:
            user = customer.objects.get(username=login_username)
        except:
            user = None
        if user is not None and user.password == login_password:
            return redirect( '')    
        else:
            return redirect( '/login/')






# Create your views here.