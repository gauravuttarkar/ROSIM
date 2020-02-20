from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from tasks.models import Clients, Tasks, Images
from django.contrib import messages

def index(request):
	print(request.user)
	print("Hitting Home Page Successfull")
	data = {
	    'name': 'Vitor',
	    'location': 'Finland',
	    'is_active': True,
	    'count': 28
	}
	#return JsonResponse(data)
	#return HttpResponse("Done and dusted")
	return render(request,'home.html',{'user':request.user})

def registration(request):
	name = "Unnamed"
	mac = request.POST.get('MAC')
	if request.POST.get('Name'):
		name = request.POST.get('Name')
	print(mac)
	Clients.objects.create(mac=mac, name=name)
	
	return HttpResponse("Done and dusted")

def ImageDeployment(request):
	client = request.POST.get('client')
	print(client)
	imageName = request.POST.get('imageName')
	print(imageName)
	clientInstance = Clients.objects.get(mac=client)
	imageInstance = Images.objects.get(imageName=imageName)
	print(clientInstance.mac)
	Tasks.objects.create(client=clientInstance, taskType='ImageDeployment', imageName=imageInstance)
	messages.success(request, 'Your task was created successfully!') 
	return redirect('/tasks/'+client)
	#return HttpResponse("Done and dusted")

def getTasks(request):
	mac = request.POST.get('MAC')
	tasks = Tasks.objects.all().filter(client=mac)
	print(tasks)
	listOfTasks = []

	for task in tasks:
		print(task.imageName)
		di = {}
		di['id'] = task.id
		di['taskType'] = task.taskType
		di['imageName'] = task.imageName.imageName
		listOfTasks.append(di)

	print(listOfTasks)
	data = {
	'tasks' : listOfTasks
	}
	return JsonResponse(data)
	#return HttpResponse("Done and dusted")

def taskStatus(request):
	mac = request.POST.get('MAC')
	status = request.POST.get('status')
	if status == '0':
		task = Tasks.objects.get(client=mac).delete()

	return HttpResponse("Task status updated")

def listClients(request):
	clientObjects = Clients.objects.all()
	# listOfImages = Images.objects.all()
	#return HttpResponse("List of Clients")
	return render(request,'clients.html',{'clientlist':clientObjects})

def clientDetails(request,mac):
	clientInstance = Clients.objects.get(mac=mac)
	listOfImages = Images.objects.all()
	print(clientInstance)
	return render(request,'clientdetail.html',{'client':clientInstance, 'imagelist':listOfImages })

