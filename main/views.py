from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile
# from .forms import ProfileRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.all().count()
    # num_genres = Genre.objects.all().count()
    # num_books_with_word = Book.objects.filter(title__contains='ebola').count()

    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            # 'num_books': num_books,
            # 'num_instances': num_instances,
            # 'num_instances_available': num_instances_available,
            # 'num_authors': num_authors,
            # 'num_genres': num_genres,
            # 'num_books_with_word': num_books_with_word,
            # 'num_visits': num_visits
        },
    )


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
