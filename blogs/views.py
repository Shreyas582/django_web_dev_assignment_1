from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Blog
from .models import Blog as BlogModel
from django.views.generic.edit import DeleteView 

@login_required()
def home(request):
    blog = Blog()
    
    if request.method == 'POST':
        blog = Blog(request.POST)
        if blog.is_valid():
            blog.save()
            return redirect('/blogs/home/')

    blogs = BlogModel.objects.filter(created_by=request.user.id)
    
    return render(request, 'blogs.html', {'form': blog, 'blogs': blogs })

class BlogDeleteView(DeleteView):
    model = BlogModel 
    success_url = '/blogs/home/'