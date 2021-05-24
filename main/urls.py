from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# User operations
urlpatterns += [
    url(r'^accounts/create/$', views.user_registration, name='profile_create')
]

# Profile operations
urlpatterns += [
    # url(r'^profile/create/$', views.ProfileCreate.as_view(), name='profile_create'),
    # url(r'^profile/(?P<pk>\d+)/update/$', views.ProfileUpdate.as_view(), name='profile_update'),
    # url(r'^profile/(?P<pk>\d+)/delete/$', views.ProfileDelete.as_view(), name='profile_delete'),
    # url(r'^signup/$', views.signup, name='signup')
    # url(r'^profile/registration/$', views.profile_registration, name='profile_create')
]
