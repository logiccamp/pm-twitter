from django.http import request
from django.shortcuts import render

# Create your views here.
def homepage (request):
    return render (request, 'twitter/index.html')