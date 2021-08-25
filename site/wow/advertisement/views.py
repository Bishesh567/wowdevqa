from django.shortcuts import render
from django.http import HttpResponse
from advertisement.models import database

# Create your views here.
def index(request):
    return render(request, 'home.html')

def sign(request):

    return render(request, 'sign.html')

def log(request):
    if request.method == "POST":
        name = request.POST['FirstName']
        sur_name = request.POST['lastName']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['pass']
        # gender = request.POST['sex']

        var = database(name=name, last_name=sur_name, age=age, email=email, password=password)
        var.save()
    fetch = database.objects.all()
    emaill = []
    for i in fetch:
        emaill.append(i.email)

    return render(request, 'login.html',{'email': emaill})

def dashboard(request):

    return render(request, 'dashboard.html')

