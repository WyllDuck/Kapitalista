from django.shortcuts import render

def index (request):
    return render( request, "home/home.html")

def conclusion (request):
    return render( request, "home/conclusion.html")
    