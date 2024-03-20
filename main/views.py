from django.shortcuts import render
from .models import *

def index_view(request):
    context = {
        'banner' : Banner.objects.last(),
        'r_experience': Experience.objects.all().order_by('-id')[:2],
        'l_experience': Experience.objects.all().order_by('-id')[2:4],
        'awards' : Awards.objects.all().order_by('-id')[:2],
        'contact' : Contact.objects.last()
    }
    return render(request,'index.html', context)

