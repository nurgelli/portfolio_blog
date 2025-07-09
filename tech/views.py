from django.shortcuts import render, redirect, get_object_or_404
from .models import Tech
from django.views import View
from .forms import TechForm

# Create your views here.

class Tech_list(View):
    
    def get(self, request):
        techs = Tech.objects.all()
        return render(request, 'tech/tech_list.html', {"techs": techs})
    
class Tech_detail(View):
    
    def get(self, request, id):
        tech = Tech.objects.get(id=id)
        return render(request, 'tech/tech_detail.html', {"tech": tech})
    

class Create_tech(View):
    tech_form = TechForm
    tech_template = 'tech/create_tech.html'
    
    def get(self, request):
        return render(request, self.tech_template, {'form': self.tech_form})
    
    def post(self, request):
        form = TechForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tech:list')
        return render(request, self.tech_template, {"form": form})
    
class Update_tech(View):
   tech_form = TechForm
   tech_template = 'tech/create_tech.html'
   
   def get(self, request, id):
       tech = get_object_or_404(Tech, id=id)
       return render(request, self.tech_template, {"form": self.tech_form(instance = tech)})
   
   def post(self, request, id):
       tech = get_object_or_404(Tech, id=id)
       form = TechForm(request.POST, instance=tech)
       if form.is_valid():
           form.save()
           return redirect('tech:detail', id=tech.id)
       return render(request, self.tech_template, {'form': form})      # form -> {{form.as_p}}
   


class Delete_tech(View):
    tech_template = 'tech/confirm.html'
    
    def get(self, request, id):
        tech = get_object_or_404(Tech, id=id)
        return render(request, self.tech_template, {"tech": tech})
    def post(self, request, id):
        Tech.objects.filter(id=id).delete()
        return redirect('tech:list')
        
        
        
    