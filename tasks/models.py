from django.db import models

# Create your models here.
class Clients(models.Model):
	mac = models.CharField(primary_key=True, max_length=50)
	name = models.CharField(max_length=20, null=True,default=None)

class Tasks(models.Model):
	client = models.ForeignKey(Clients,on_delete=models.CASCADE)
	imageName = models.CharField(max_length=20, null=False, default=None)
	taskType = models.CharField(max_length=20, null=False, default=None)