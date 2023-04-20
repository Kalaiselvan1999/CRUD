from django.shortcuts import render, redirect
from .forms import EmpForm, DeptForm
from .models import Department,Employee
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmpForm()
    context = {
        'form':form
    }
    return render(request, 'create emp.html', context)

def create_dept(request):
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    else:
        form = DeptForm()
    context = {"form":form}
    return render(request, 'create_dept.html', context)


def view(request, id):
    obj1 = Employee.objects.filter(department_id = id)
    obj2 = Department.objects.filter(id = id)
    if obj1 or obj2:
        content = {"dept":obj2,"emp":obj1}
        return render(request,'read.html',content)
    else:
        return render(request, 'read.html', {"emp":obj1,"dept":obj2})


     
def update(request, id):
    obj = Employee.objects.filter(id = id).first()
    if obj is not None:
        if request.method == "POST":
            form = EmpForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = EmpForm()
        context = {"form":form,"data":obj}
        return render(request, 'update.html', context)
    else:
        return render(request, 'update.html',{'data':False})

def delete(request, id):
    obj = Employee.objects.filter(id = id).first()
    if obj is not None:
        obj.delete()
        return render(request, 'delete.html', {"obj":obj})
    else:
        return render(request, 'delete.html', {"obj":False})
