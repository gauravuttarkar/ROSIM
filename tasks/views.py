from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from tasks.models import Clients, Tasks, Images, Deployment, Cloning, Partitions
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
	taskInstance = Tasks.objects.create(client=clientInstance, taskType='ImageDeployment')
	Deployment.objects.create(taskId=taskInstance,imageName=imageInstance)
	messages.success(request, 'Your task was created successfully!') 
	return redirect('/tasks/'+client)
	#return HttpResponse("Done and dusted")

def cloning(request):
	client = request.POST.get('client')
	partitionName = request.POST.get('partitionName')
	print(client)
	
	partitions = request.POST.getlist('partitions[]')
	print(partitions)	
	print(partitionName)
	
	# client = '08-00-27-1c-71-6c'
	clientInstance = Clients.objects.get(mac=client)
	# partitionName = 'TestPartition'
	# partitions = [1,2,3]
	taskInstance = Tasks.objects.create(client=clientInstance, taskType='Cloning')
	cloningInstance = Cloning.objects.create(taskId=taskInstance,partitionName=partitionName)
	for partition in partitions:
		Partitions.objects.create(cloningId=cloningInstance,partitionNumber=partition)
	messages.success(request, 'Your task was created successfully!') 
	return HttpResponse("Done and dusted")


def getTasks(request):
	mac = request.POST.get('MAC')
	task = Tasks.objects.get(client=mac)
	print(task)
	
	di = {}
	di['id'] = task.id
	di['taskType'] = task.taskType

	if di['taskType'] == 'Cloning':
		cloningInstance = Cloning.objects.get(taskId=task)
		print(cloningInstance)
		di['partitionName'] = cloningInstance.partitionName
		partitions = Partitions.objects.all().filter(cloningId=cloningInstance)
		print(partitions)
		listOfPartitions = []
		for i in partitions:
			listOfPartitions.append(i.partitionNumber)
		print(listOfPartitions)
		di['partitionNumber'] = listOfPartitions
		
	if di['taskType'] == 'ImageDeployment':
		deploymentInstance = Deployment.objects.get(taskId=task)
		print(deploymentInstance.imageName.imageName)
		di['imageName'] = deploymentInstance.imageName.imageName
	# for task in tasks:
	# 	print(task.imageName)
	# 	di = {}
	# 	di['id'] = task.id
	# 	di['taskType'] = task.taskType
	# 	di['imageName'] = task.imageName.imageName
	# 	listOfTasks.append(di)
	print(di)
	# print(listOfTasks)
	# data = {
	# 'tasks' : listOfTasks
	# }
	return JsonResponse(di)
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

