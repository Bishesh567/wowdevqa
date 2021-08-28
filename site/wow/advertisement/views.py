from django.shortcuts import render
from django.http import HttpResponse
from advertisement.models import database
from advertisement.models import File

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

    return render(request, 'login.html')




def dashboard(request):
    fetch = database.objects.all()
    emaill = []
    passwordd = []
    for i in fetch:
        emaill.append(i.email)
        passwordd.append(i.password)
    if request.method == "POST":
        email = request.POST['emel']
        password = request.POST['pas']
    j = 0;
    for i in emaill:
        if email == i and password == passwordd[j]:
            return render(request, 'dashboard.html')
        j += 1;
    else:
        return render(request, 'login.html')

def dash(request):
    if request.method == "POST":
        data = request.POST['files']
        fil = File(file = data)
        fil.save()
    return render(request, 'dashboard.html')