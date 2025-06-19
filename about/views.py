from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    context = About.objects.all()
    
    return render(request, 'about/index.html', {'context': context})
