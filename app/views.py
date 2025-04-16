from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees , many = True)
            return  JsonResponse(serializer.data , safe = False)
    elif request.method == 'POST':
          jsonData = JSONParser().parse(request)
          serializer = EmployeeSerializer(data = jsonData)
          if serializer.is_valid():
               serializer.save()
               return  JsonResponse(serializer.data, safe = False)
          else:
               return JsonResponse(serializer.errors , safe = False)


def home_page(request):
    return HttpResponse("hello django")
  
def UserListView(request):
    users = User.objects.all()
    Userdata = UserSerializer(users , many = True)
    return JsonResponse( Userdata.data , safe = False)


def employeeDetailView(request , pk):
     if request.method == 'DELETE':
          pass
     elif request.method == 'GET':
          pass
     elif request.method == 'PUT':
          pass