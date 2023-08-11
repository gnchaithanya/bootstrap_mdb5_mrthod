from django.shortcuts import render

# Create your views here.
def mdb5(request):
    return render(request,'mdb5.html')
def carousel(request):
    return render(request,'carousel.html')
def background_image(request):
    return render(request,'background_image.html')
def dropdowns(request):
    return render(request,'dropdowns.html')