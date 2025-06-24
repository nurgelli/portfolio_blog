from django.forms import ModelForm
from .models import About


class AboutForm(ModelForm):
    
    class Meta:
        model = About
        fields = '__all__'