from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.views import generic

# Create your views here.

class Job_list(generic.ListView):
    queryset = Job.objects.all()
    template_name = 'job/job_list.html'
    
class Job_detail(generic.DetailView):
    model = Job
    template_name = 'job/job_detail.html'

