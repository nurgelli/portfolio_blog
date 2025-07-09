from django.forms import ModelForm
from .models import Tech


class TechForm(ModelForm):
    class Meta: 
        model = Tech
        fields = '__all__'