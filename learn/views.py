from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'home.html')
    #return HttpResponse(u"Hello world!")

def home(request):
    string = "Test 测试"
    return render(request, 'home.html', {'string': string})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add3(request, a, b):
    return HttpResponseRedirect(reverse('add3', args=(a, b)))