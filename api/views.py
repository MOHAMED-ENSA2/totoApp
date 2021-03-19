from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task 
from .serializers import TaskSerialzer 


# Create your views here.

@api_view(['GET'])
def apiOverviews(request):
	api_urls = {
		"list of tasks" : 'task-list/' , 
		"detail view" : 'task-detail/<str:pk>/' , 
		"create" : 'task-create/' ,
		"update" :'task-update/<str:pk>' ,
		"delete" : 'task-delete/<str:pk>' ,

	}
	return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
	tasks = Task.objects.all()
	serializer = TaskSerialzer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
	tasks = Task.objects.get(id = pk )
	serializer = TaskSerialzer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def TaskCreate(request):
	serializer = TaskSerialzer(data = request.data)
	if serializer.is_valid() : 
		serializer.save()
	return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request,pk):
	task = Task.objects.get(id = pk )
	serializer = TaskSerialzer(instance =task  , data = request.data)
	if serializer.is_valid() : 
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request,pk):
	task = Task.objects.get(id = pk )
	task.delete()
	return Response("Item deleted")