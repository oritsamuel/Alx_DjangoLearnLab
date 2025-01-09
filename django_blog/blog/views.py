from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from registration.backends.simple.views import RegistrationView

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


class MyRegistrationView(RegistrationView):
    form_class = UserCreationForm  # Or your custom registration form
    template_name = 'registration/register.html'  # Your registration template

    def get_success_url(self, user=None):
        login(self.request, user)  # Log in the user after registration
        return reverse('your_profile_view_name')  # Redirect to profile page

def register(request):
    if request.method == 'POST':
        form = MyRegistrationView.form_class(request.POST)
        if form.is_valid():
            form.save()
            return MyRegistrationView.get_success_url(self)
    else:
        form = MyRegistrationView.form_class()
    return render(request, 'registration/register.html', {'form': form})