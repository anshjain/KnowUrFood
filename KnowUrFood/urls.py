"""KnowUrFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import views as auth

admin.site.site_header = _("Know Ur Food administration")
admin.site.site_title = _("Know Ur Food admin")
admin.site.index_title = _("Manage Know Ur Food")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("lang/", include("django.conf.urls.i18n")),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('login/', auth.LoginView.as_view(template_name='profile/login.html'), name='login'),
]

urlpatterns += i18n_patterns(
    path('', include('product.urls')),
    path('profile/', include('UserProfile.urls')),
    prefix_default_language=False
)
