from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Funcion-based view


def employeeView(request):
    # emp = {'id': 123, 'name': 'John', 'salary': 1000000} - just a reference from the previous code

    data = Employee.objects.all()
    response = {'employees':list(data.values('name', 'sal'))}
    return JsonResponse(response)
