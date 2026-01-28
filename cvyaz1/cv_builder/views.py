from django.shortcuts import render

def index(request):
    return render(request, "cv_builder/index.html")
