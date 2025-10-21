from django.shortcuts import render,redirect
from .form import user

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,login_not_required,permission_required

from django.http import HttpResponse

# Create your views here.
@login_not_required
def register(request):
   in1 = {"username":"","email":"","password1":"","password2":"","first_name":"","last_name":""}
   if request.method=='POST':
        form = user(request.POST)
        if form.is_valid():
            form.save()
            user1 = form.cleaned_data.get('username')
            messages.success(request, f"user {user1} account has successfully created.")
            return redirect('login')
        
   else:
        form=user(initial=in1)

   context={'from':form}
   return render(request,"register from.html",context)

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import CustomLoginForm

def login_view(request):
    next_url = request.GET.get('next') or request.POST.get('next') or '/' # fallback

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = CustomLoginForm()

    context = {
        'form': form,
        'next': next_url
    }
    return render(request, 'login.html', context)

@login_required()
def logout_view(request):
    messages.success(request,'you have been logout')
    logout(request)
    return redirect('login')



