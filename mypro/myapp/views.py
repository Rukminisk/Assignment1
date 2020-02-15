from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Test1(request):
    return HttpResponse('<h1> National Centre for Biological sciences</h1>')
def Test2(request):
    return HttpResponse('<h1> Tata Instutute for Fundamental Research </h1>')
def Test3(request):
    return HttpResponse('<h1> Center for Cellular and Molecular Platforms</h1>')