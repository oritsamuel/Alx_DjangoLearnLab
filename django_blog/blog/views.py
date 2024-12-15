from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()
def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')  # Redirect to login page after successful registration
  else:
    form = RegistrationForm()
  return render(request, 'registration.html', {'form': form})

@login_required  # Restrict access to logged-in users
def profile(request):
  user = get_object_or_404(User, pk=request.user.pk)
  # ... Handle user details and update logic
  return render(request, 'profile.html', {'user': user})