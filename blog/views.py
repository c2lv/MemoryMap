from django.shortcuts import render
from django.views import generic
from .models import Mapmodel


# Create your views here.
def main(request):
    return render(request, 'main.html')


def blogHome(request):
    blogdata = Mapmodel.objects
    return render(request, 'blogHome.html', {'blogdata':blogdata})

