from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
	print(request.user)
	print("Hitting Home Page Successfull")
	data = {
	    'name': 'Vitor',
	    'location': 'Finland',
	    'is_active': True,
	    'count': 28
	}
	return JsonResponse(data)
	#return HttpResponse("Done and dusted")
	#return render(request,'home1.html',{'user':request.user})