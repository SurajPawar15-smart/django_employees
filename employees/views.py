from django.shortcuts import render,get_object_or_404,redirect
from . models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def employee_detail(request,id):
    employee=get_object_or_404(Employee,id=id)
    context={
        'employee':employee
    }
    return render(request,'employee_detail.html',context)

@login_required
@permission_required('employees.add_employee',raise_exception=True)
def add_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
        else:
            print(form.errors)
    form=EmployeeForm()
    context={'form':form}
    return render(request,'add_employee.html',context)


# Edit Employee
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)

    context = {'form': form, 'employee': employee}
    return render(request, 'edit_employee.html', context)


# Delete Employee
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('home')

    return render(request, 'confirm_delete.html', {'employee': employee})

# View Employee Details
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {'employee': employee}
    return render(request, 'employee_detail.html', context)