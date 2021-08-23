from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'home.html')

def sign(request):

    return render(request, 'sign.html')

def log(request):
    return render(request, 'login.html')