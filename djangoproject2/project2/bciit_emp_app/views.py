from django.shortcuts import render
from django.http import HttpResponse
from .import views
from .models import Employee
# Create your views here.

def index(request):
    dict={'h':'gello','m':'hello'}
    return render(request,'bciit_emp_app/index.html',dict)

def all_emp(request):
    emps=Employee.objects.all()
    
    #print(context)
    return render(request,'bciit_emp_app/all.html',{'emp':emps})
def  add_emp(request):
    return render (request,'bciit_emp_app/index.html',dict)

def  remove_emp(request):
    return render (request,'bciit_emp_app/index.html',dict)

def  filter_emp(request):
    return render (request,'bciit_emp_app/index.html')


