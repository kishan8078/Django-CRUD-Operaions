import json
from django.shortcuts import render,redirect
from .models import tasks
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.

#method that returns page below
def home(request):

    allTask=tasks.objects.all()
    print(allTask)

    context={'allTask':allTask}
    return render(request,'index.html',context)    
    

#method that returns only the data below
# def home(request):

#     all_tasks = tasks.objects.all()

#     serialized_tasks = serialize('json', all_tasks)
#     parsed_tasks = json.loads(serialized_tasks)

#     return JsonResponse({'tasks': parsed_tasks}, safe=False)



def addTask(request):
    if request.method=='POST':
        newTask=request.POST['newTask']
    context={'newAddedTask':newTask}
    print(newTask)

    query=tasks(task=newTask)
    query.save()
    
    allTask=tasks.objects.all()

    print(allTask,"from db")
    context={'allTask':allTask}
    
    return render(request,'index.html',context)

def editTask(request,taskId):
    taskToBeEdited=tasks.objects.get(taskId=taskId)

    

    allTask=tasks.objects.all()
    context={'allTask':allTask,'taskToBeEdited':taskToBeEdited}
    
    return render(request,'index.html',context)

def updateTask(request,taskId):
    taskToBeUpdated=tasks.objects.get(taskId=taskId)

    taskToBeUpdated.task=request.POST['updatedTask']
    taskToBeUpdated.save()

    return home(request)

def deleteTask(request,taskId):
    taskToBeDeleted=tasks.objects.get(taskId=taskId)

    taskToBeDeleted.delete()

    return home(request)