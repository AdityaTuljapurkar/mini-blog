from django.shortcuts import render
from django.http import HttpResponse
from .models import data

# Create your views here.

def index (request):
    posts = data.objects.all()
    return render(request,"index.html", {'posts':posts})

def post(request,pk):
    posts= data.objects.get(id=pk)
    return render(request,"post.html",{"post":posts})





















































