from django.shortcuts import render

def events(request):
    return render(request,'eventsList.html')