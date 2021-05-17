"""URL-конфигурация"""
from django.contrib import admin
from django.conf.urls import include
from django.shortcuts import redirect
from django.urls import path


def admin_redirect(request):
    return redirect('/admin', permanent=True)


urlpatterns = [
    path('', admin_redirect),
    path('api/', include('api.urls')),
    # apps' views' urls must be before admin url patterns!
    path('admin/', admin.site.urls)
]
