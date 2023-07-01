from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # print(request)
    # return HttpResponse('<h1>HTTP RESPONSE</h1> Template')
    return render(request, 'teste.html')

def add(request):

    return render(request, 'app.html')