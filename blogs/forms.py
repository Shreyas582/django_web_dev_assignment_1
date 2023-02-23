from django.forms import ModelForm
from .models import Blog 

class Blog(ModelForm):
    class Meta:
        model = Blog 
        fields = ['blog_title', 'content',]
