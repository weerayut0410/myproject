from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product

# Create your views here.
def db(request):
    all_product = Product.objects.all
    some_product = Product.objects.filter(price__gt=5000)
    return render(request, 'db.html',{"all_product":all_product,'some_product':some_product})

def Index(request):
    name = 'John Doe'
    age = 42
    return render(request, 'index.html',{"name":name,"age":age})

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

