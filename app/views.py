from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cssShapes(request):
    return render(request, 'cssShapes.html')
