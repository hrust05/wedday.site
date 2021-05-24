from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


def index(request):
    return render(
        request,
        'index.html',
        context={},
    )


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # user.username = form.cleaned_data.get('username')
            # user.email = form.cleaned_data.get('email')
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/create_user.html', {'form': form})

# class ProfileCreate(CreateView):
#     model = Profile
#     user_form = UserForm
#     profile_form = ProfileForm
#     fields = '__all__'
#
#
# class ProfileUpdate(LoginRequiredMixin, UpdateView):
#     model = Profile
#     fields = '__all__'
#
#
# class ProfileDelete(LoginRequiredMixin, DeleteView):
#     model = Profile
#     # success_url = reverse_lazy('authors')


# def profile_registration(request):
#     if request.method == 'POST':
#         form = ProfileRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profile instance created by the signal
#             user.profile.phone_number = form.cleaned_data.get('phone_number')
#             user.profile.email = form.cleaned_data.get('email')
#             user.profile.birth_date = form.cleaned_data.get('birth_date')
#             user.profile.location = form.cleaned_data.get('location')
#             user.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = ProfileRegistrationForm()
#     return render(request, 'accounts/profile_create.html', {'form': form})
