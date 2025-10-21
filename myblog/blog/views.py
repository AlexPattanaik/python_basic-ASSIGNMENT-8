from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from .models import blog
from .forms import blog_from
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required()
def blog_from_view(request):

    form=blog_from(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return redirect('blog')
    context ={
        'form':form
    }

    return render(request,'add_blog.html',context)



def blog_view(request):
    blog_lst = blog.objects.all()
    context={
        'blog_lst':blog_lst
    }

    return render(request,'blog.html',context)
def blog_detail_view(request,id):
    blog_full=blog.objects.get(id=id)
    context={'blog_full':blog_full}
    return render(request,'blog_detail_view.html',context)
