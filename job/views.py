from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.

class Job_list(ListView):
    queryset = Job.objects.all()
    template_name = 'job/job_list.html'
    
class Job_detail(DetailView):
    model = Job
    template_name = 'job/job_detail.html'
    

