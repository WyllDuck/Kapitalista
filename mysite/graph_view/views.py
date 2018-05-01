from django.shortcuts import render

def graph_1 (request):
    return render(request, "graph_view/graph_1.html")

def graph_2 (request):
    return render(request, "graph_view/graph_2.html")

def graph_3 (request):
    return render(request, "graph_view/graph_3.html")

def general (request):
    return render(request, "graph_view/general_analysis.html")
    
