from django.shortcuts import render

# Create your views here.

def home(request):
    print("hi")
    # print(request.data)
    return render(request, 'index.html') 