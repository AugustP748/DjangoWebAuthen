from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,"main/home.html")
	#return HttpResponse("Hello world")

