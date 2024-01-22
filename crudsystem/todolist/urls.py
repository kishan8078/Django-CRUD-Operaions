
from django.urls import path
from todolist import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.addTask,name='addTask'),
    path('edit/<int:taskId>',views.editTask,name="editTask"),
    path('update/<int:taskId>',views.updateTask,name="updateTask"),
    path('delete/<int:taskId>',views.deleteTask,name="deleteTask")
]
