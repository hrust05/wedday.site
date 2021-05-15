from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile
from .forms import UserForm, ProfileForm, SignUpForm
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

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно создан!')
            return redirect('settings:profile')
        else:
            messages.error(request, 'Указанные Вами данные содержат ошибки.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/profile_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.location = form.cleaned_data.get('location')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.phone_number = form.cleaned_data.get('phone_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'profile/signup.html', {'form': form})

# @login_required
# @transaction.atomic
