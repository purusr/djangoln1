from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from django.shortcuts import render, redirect

def index(request):
    stdata = Student.objects.all()
    return render(request, 'polls/index.html', {'Studentlist':stdata})
