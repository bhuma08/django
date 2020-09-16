from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.
def signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome, {username}!')
            return redirect ('book-index')
        else:  # form is not valid
            return HttpResponse("Form is not valid")
        
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, 'users/signup.html', data)
