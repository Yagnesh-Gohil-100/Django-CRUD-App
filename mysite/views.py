from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):

  #if already logged in...
  records = Record.objects.all()

  # check login activity
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    # Authentication

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "Login successful...")
    else:
      messages.success(request, "Error occured during logging in, Please try again...")
    
    return redirect('home')
  # if not post request
  else:
    return render(request, 'home.html', {'records':records})
  

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()

      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']

      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, "Your registration is done successfully!")
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form':form})
  
  return render(request, 'register.html', {'form':form})


def individual_record(request, pk):
  if request.user.is_authenticated:
    record = Record.objects.get(id=pk)
    return render(request, 'individual_record.html', {'record':record})
  else:
    messages.success(request, "You cannot see the page, login first to see the content of the page!")
    return redirect('home')
  
def delete_record(request, pk):
  if request.user.is_authenticated:
    delete_rec = Record.objects.get(id=pk)
    delete_rec.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect('home')
  else:
    messages.success(request, "You cannot see the page, login first to see the content of the page!")
    return redirect('home')

def add_record(request):
  form = AddRecordForm(request.POST or None)
  if request.user.is_authenticated:
    if request.method == "POST":
      if form.is_valid():
        form.save()
        messages.success(request, "Record added successfully!")
        return redirect('home')
    return render(request, 'add_record.html', {'form':form})
  else:
    messages.success(request, "You cannot access the page, login first to see the content of the page!")
    return redirect('home')
  
def update_record(request, pk):
  if request.user.is_authenticated:
    current_data = Record.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=current_data)
    if request.method == "POST":
      if form.is_valid():
        form.save()
        messages.success(request, "Record Updated successfully!")
        return redirect('home')
    else:
      return render(request, 'update_record.html', {'form':form})
  else:
    messages.success(request, "You cannot access the page, login first to see the content of the page!")
    return redirect('home')
  