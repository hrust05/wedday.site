# from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# User
urlpatterns += [
    url(r'^accounts/register/$', views.user_registration, name='user_register'),
    url(r'^accounts/(?P<pk>[-\w\d]+)/detail$', views.user_detail_view, name='user_detail'),
    url(r'^accounts/(?P<pk>[-\w\d]+)/update$', views.user_update_view, name='user_update'),
]

# Profile
urlpatterns += [
    url(r'^profile/(?P<pk>[-\w\d]+)/create/$', views.profile_create, name='profile_create'),
    # url(r'^profile/detail/(?P<pk>\d+)$', views.ProfileDetailView.as_view(), name='profile_detail'),
    # url(r'^profile/list/$', views.ProfileListView.as_view(), name='profile_list'),
    # url(r'^profile/create/$', views.ProfileCreate.as_view(), name='profile_create'),
    # url(r'^profile/(?P<pk>\d+)/update/$', views.ProfileUpdate.as_view(), name='profile_update'),
    # url(r'^profile/(?P<pk>\d+)/delete/$', views.ProfileDelete.as_view(), name='profile_delete'),
    # url(r'^signup/$', views.signup, name='signup')
    # url(r'^profile/registration/$', views.profile_registration, name='profile_create')
]

# Catalog
urlpatterns += [
    url(r'catalog/$', views.CatalogListView.as_view(), name='catalog'),
]

# Under construction
urlpatterns += [
    url(r'under-construction/$', views.under_construction, name='under_construction'),
]
