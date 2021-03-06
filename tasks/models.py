from django.db import models

# Create your models here.
class Clients(models.Model):
	mac = models.CharField(primary_key=True, max_length=50)
	name = models.CharField(max_length=20, null=True,default=None)

class Images(models.Model):
	imageName = models.CharField(max_length=20, null=False, default=None, unique=True)

class Tasks(models.Model):
	client = models.ForeignKey(Clients,on_delete=models.CASCADE,unique=True)
	taskType = models.CharField(max_length=20, null=False, default=None)

class Deployment(models.Model):
	taskId = models.ForeignKey(Tasks,on_delete=models.CASCADE)
	imageName = models.ForeignKey(Images,on_delete=models.CASCADE)

class Cloning(models.Model):
	taskId = models.ForeignKey(Tasks,on_delete=models.CASCADE)
	partitionName = models.CharField(max_length=20, null=False, default=None)

class Partitions(models.Model):
	cloningId = models.ForeignKey(Cloning,on_delete=models.CASCADE)
	partitionNumber = models.CharField(max_length=20, null=False, default=None)