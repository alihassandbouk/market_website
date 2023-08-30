from django.shortcuts import render, redirect
from .forms import SignForm
from item.models import *


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html",{
        "categories":categories,
        "items":items
    })

def contact(request):
    return render(request,"core/contact.html")

def signup(request):
    if request.method =='POST' :
        form = SignForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
    else:
        form = SignForm()



    return render(request, "core/signup.html",{
        'form':form
    })






