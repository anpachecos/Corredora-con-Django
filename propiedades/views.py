from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def slide1(request):
    return render(request, 'slide-1.jpg')