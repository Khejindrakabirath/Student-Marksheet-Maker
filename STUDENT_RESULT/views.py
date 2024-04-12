from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from STUDENT_RESULT import forms

from STUDENT_RESULT.models import studentModel
from .forms import addForm
# Create your views here.

def homepage(request):
    model = studentModel.objects.all()
    return render(request,'resultChart.html',{'model': model})

def add(request):
    addform = addForm()
    if request.method=='POST':
        addform = addForm(request.POST)
        if addform.is_valid():
            addform.save()
            return redirect('/add')
    return render(request,'add.html',{'form':addform})

def resultDetails(request,id):
    model = studentModel.objects.filter(id = id)
    return render(request,'resultDetails.html',{'model': model})

def update(request,id):
    addmodel = studentModel.objects.get(id = id)
    addforms = addForm(instance = addmodel)
    if request.method == "POST":
        addforms = addForm(request.POST,instance = addmodel)
        if addforms.is_valid():
            addforms.save()
            return redirect('homepage')
    return render(request,'update.html',{'addforms': addforms})

def delete(request,id):
    modela = studentModel.objects.get(id = id)
    modela.delete()
    return redirect("/")

