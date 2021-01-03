from django.shortcuts import render
from django.http import JsonResponse

# Funcion-based view


def employeeView(request):
    emp = {'id': 123, 'name': 'John', 'salary': 1000000}
    return JsonResponse(emp)
