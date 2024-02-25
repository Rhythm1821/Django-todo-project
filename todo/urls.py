from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("apis/v1/",include('apis.urls')),
    path('', RedirectView.as_view(url='/apis/v1/')),
]
