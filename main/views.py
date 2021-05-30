from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm, ProfileRegistrationForm
# from django.views import generic
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ProfessionInstance, Profile, Profession, SiteUser
from django.views.generic.list import ListView


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
            user.phone_number = form.cleaned_data.get('phone_number')
            user.email = form.cleaned_data.get('email')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.birth_date = form.cleaned_data.get('birth_date')
            user.location = form.cleaned_data.get('location')
            user.description = form.cleaned_data.get('description')
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/user_register.html', {'form': form})


def user_detail_view(request, pk):
    try:
        user_id = SiteUser.objects.get(pk=pk)
    except SiteUser.DoesNotExist:
        raise Http404("Указанного пользователя не существует")

    # user_id = get_object_or_404(SiteUser, pk=pk)

    if Profile.objects.filter(user=user_id).exists():
        return render(request, 'user/user_detail.html',
                      context={'user': user_id, 'profile': Profile.objects.get(user=user_id), })
    else:
        return render(request, 'user/user_detail.html', context={'user': user_id})


def user_update_view(request, pk):
    try:
        user = SiteUser.objects.get(pk=pk)
    except SiteUser.DoesNotExist:
        raise Http404("Указанного пользователя не существует")

    if not request.user == user:
        raise Http404("Такой страницы не существует")

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            user.phone_number = form.cleaned_data.get('phone_number')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.birth_date = form.cleaned_data.get('birth_date')
            user.description = form.cleaned_data.get('description')
            user.location = form.cleaned_data.get('location')
            user.save()
            if Profile.objects.filter(user=user).exists():
                return render(request, 'user/user_detail.html',
                              context={'user': user, 'profile': Profile.objects.get(user=user), })
            else:
                return render(request, 'user/user_detail.html', context={'user': user})
    else:
        form = UserUpdateForm()

    if Profile.objects.filter(user=user).exists():
        return render(request, 'user/user_update.html',
                      context={'form': form, 'user': user, 'profile': Profile.objects.get(user=user), })
    else:
        return render(request, 'user/user_update.html',
                      context={'form': form, 'user': user})


def profile_create(request, pk):
    try:
        user = SiteUser.objects.get(pk=pk)
    except SiteUser.DoesNotExist:
        raise Http404("Указанного пользователя не существует")

    if not request.user == user:
        raise Http404("Такой страницы не существует")

    professions = Profession.objects.all()
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                if Profile.objects.filter(user=request.user).exists():
                    profile = Profile.objects.get(user=request.user)
                else:
                    profile = form.save(commit=False)
                    profile.user = request.user
                    profile.save()

                selected_professions = request.POST.getlist('professions')
                for profession in selected_professions:
                    profession_name = professions.get(name=profession)
                    # profession_name = Profession.objects.get(name=profession)
                    if not ProfessionInstance.objects.filter(profession=profession_name, userprofile=profile).exists():
                        pr_instance = ProfessionInstance(
                            profession=profession_name,
                            userprofile=profile,
                            rating=0)
                        pr_instance.save()
                if Profile.objects.filter(user=profile.user).exists():
                    return render(request, 'user/user_detail.html',
                                  context={'user': profile.user, 'profile': Profile.objects.get(user=profile.user), })
                else:
                    return render(request, 'user/user_detail.html', context={'user': profile.user})
    else:
        form = ProfileRegistrationForm()
    # return render(
    #     request,
    #     'profile/profile_create.html',
    #     {'form': form, 'professions': professions}

    if Profile.objects.filter(user=user).exists():
        return render(request, 'profile/profile_create.html',
                      context={'form': form, 'user': user, 'professions': professions,
                               'profile': Profile.objects.get(user=user), })
    else:
        return render(request, 'profile/profile_create.html',
                      context={'form': form, 'user': user, 'professions': professions, })


class CatalogListView(ListView):
    model = ProfessionInstance
    template_name = "catalog.html"
    context_object_name = 'profession_instances'
    paginate_by = 20

    # def get_ordering(self):
    #     ordering = self.request.GET.get('order_by')
    #     print(ordering)
    #     return ordering

    def get_queryset(self):
        new_context = ProfessionInstance.objects.all()

        if self.request.GET.get('order_by') != 'None':
            if self.request.GET.get('order_by'):
                order = self.request.GET.get('order_by')
                new_context = ProfessionInstance.objects.order_by(order)
            else:
                new_context = ProfessionInstance.objects.all()

        if self.request.GET.get('profession') != 'None':
            if self.request.GET.get('profession'):
                profession = self.request.GET.get('profession')
                new_context = new_context.filter(profession=profession)

        return new_context

    def get_context_data(self, **kwargs):
        context = super(CatalogListView, self).get_context_data(**kwargs)
        context['profession'] = self.request.GET.get('profession', None)
        context['order_by'] = self.request.GET.get('order_by', None)
        context['professions_list'] = Profession.objects.all()
        return context


# def catalog_view(request):
#     return render(
#         request,
#         'catalog.html',
#         context={},
#     )


def under_construction(request):
    return render(
        request,
        'under_construction.html',
        context={},
    )
