"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/',include('dpi.urls')),
    path('auth/',include('authentication.urls')),
    path('',include('ordonnance.urls')),
    path('',include('consultation.urls')),
    path('bilan-bio/',include('bilan_bio.urls')),
    path('bilan-radio/',include('bilan_radio.urls')),
    path('soins/',include('les_soins.urls')),
]
