from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'home.html')

def sign(request):

    return render(request, 'sign.html')

def log(request):
    name = request.POST['FirstName']
    sur_name = request.POST['lastName']
    age = request.POST['age']
    email = request.POST['email']
    password = request.POST['pass']
    gender = request.POST['sex']
    print(name,sur_name,age,email,password,gender)


    return render(request, 'login.html')

def dashboard(request):

    return render(request, 'dashboard.html')