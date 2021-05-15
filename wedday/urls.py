from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    # path('main/', include('main.urls')),
    # path('', RedirectView.as_view(url='/main/', permanent=True))
]
