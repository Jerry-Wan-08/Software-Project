from django.shortcuts import render

def Countries(request):
    return render(request, "Countries/main.html")
