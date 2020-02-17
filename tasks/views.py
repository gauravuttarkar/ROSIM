from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from tasks.models import Clients, Tasks

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

def registration(request):
	name = "Unnamed"
	mac = request.POST.get('MAC')
	if request.POST.get('Name'):
		name = request.POST.get('Name')
	print(mac)
	Clients.objects.create(mac=mac, name=name)
	
	return HttpResponse("Done and dusted")

def ImageDeployment(request):
	mac = request.POST.get('MAC')
	print(mac)
	imageName = request.POST.get('imageName')
	clientInstance = Clients.objects.get(mac=mac)
	Tasks.objects.create(client=clientInstance, taskType='ImageDeployment', imageName=imageName)

	return HttpResponse("Task created Successfully")

def getTasks(request):
	mac = request.POST.get('MAC')
	tasks = Tasks.objects.all().filter(client=mac)
	print(tasks)
	listOfTasks = []
	for task in tasks:
		di = {}
		di['id'] = task.id
		di['taskType'] = task.taskType
		di['imageName'] = task.imageName
		listOfTasks.append(di)

	print(listOfTasks)
	data = {
	'tasks' : listOfTasks
	}
	return JsonResponse(data)

def taskStatus(request):
	mac= request.POST.get('MAC')
	status = request.POST.get('status')
	
	if status == '0':
		task = Tasks.objects.get(client=mac).delete()




	return HttpResponse("Task status updated")

