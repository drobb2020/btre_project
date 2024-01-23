from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      # Check for unique username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is already in use.')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email address is already in use.')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(
            username=username, 
            password=password, 
            email=email,
            first_name=first_name,
            last_name=last_name
          )
          # Login after registration
          # auth.login(request, user)
          # messages.success('You are now logged in.')
          # return redirect('index')
          user.save()
          messages.success(request, 'Your account has been registered. You can now login.')
          return redirect('login')

    else:
      messages.error(request, 'Passwords do not match.')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    # Login User
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in.')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid Account.')
      return redirect('register')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('index')

def dashboard(request):
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)
