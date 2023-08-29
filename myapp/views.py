from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    name = 'John Doe'
    age = 42
    return render(request, 'index.html',{"name":name,"age":age})

def hello(request):
    return HttpResponse("<h1>Hello</h1>")
