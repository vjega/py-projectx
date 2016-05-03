from django.shortcuts import render
from projectx.models import Employee, Menus
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def employee(request):
	return render(request, 'employee.html')

