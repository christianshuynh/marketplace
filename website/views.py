from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(
        request,
        "home.html"
    )

def forsale(request):
    return render(
        request,
        "forsale.html"
    )
    
def listanitem(request):
    return render(
        request,
        "listanitem.html"
    )