from django.shortcuts import render, get_object_or_404, redirect
from .models import About
from .forms import AboutForm

# Create your views here.


def index(request):
    context = {"index": index}
    return render(request, 'index.html', context)

def project_list(request):
    projects = About.objects.all()
    return render(request, 'about/project_list.html', {'projects':projects})

def project_detail(request, id):
    project = get_object_or_404(About, id=id)
    return render(request, 'about/project_detail.html', {"project": project})

def project_create(request):
    form = AboutForm()
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about:list')
    return render(request, 'about/project_create.html', {'form': form})

def project_update(request, id):
    project = get_object_or_404(About, id=id)
    form = AboutForm(instance=project)
    if request.method == "POST":
        form = AboutForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('about:detail', id=project.id)
    return render(request, 'about/project_create.html', {"form":form})

def project_delete(request, id):
    project = get_object_or_404(About, id=id)
    if request.method == "POST":
        project.delete()
        return redirect('about:list')
    return render(request, 'about/confirm.html', {"project": project})
    