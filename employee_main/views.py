from django.http import HttpResponse
from employees.models import Employee
from django.shortcuts import render

def home(request):
    # Fetch the data from Employee tables
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'home.html', context)