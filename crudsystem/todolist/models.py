from django.db import models

# Create your models here.

class tasks(models.Model):
    taskId=models.AutoField(primary_key=True)
    task=models.CharField(max_length=50)
    taskIsDone=models.BooleanField(default=False)

    

   
