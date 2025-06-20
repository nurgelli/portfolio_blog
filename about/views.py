from django.shortcuts import render
from django.views.generic import ListView
from .models import About
# Create your views here.

# def about(request):
#     context = About.objects.all()
    
#     return render(request, 'about/index.html', {'context': context})

class About(ListView):
    model = About
    template_name = 'about/index.html'
    context = 'context'
    