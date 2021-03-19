from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.apiOverviews , name = "api-overviws"),
    path('task-list/',views.TaskList , name = "api-TaskList"),
    path('task-detail/<str:pk>/',views.TaskDetail , name = "api-detail"),
    path('task-create/',views.TaskCreate , name = "api-create"),
    path('task-update/<str:pk>/',views.TaskUpdate , name = "api-update"),
    path('task-delete/<str:pk>/',views.TaskDelete , name = "api-delete"),
   
]