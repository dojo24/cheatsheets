from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cssShapes(request):
    return render(request, 'cssShapes.html')

def jsLoops(request):
    return render(request, 'loops.html')

def jsConditionals(request):
    return render(request, 'conditionals.html')

def flexbox(request):
    return render(request, 'flexbox.html')